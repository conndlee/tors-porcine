"""Refresh manuscript snapshots from existing analysis exports without changing the source."""

import argparse
import csv
import hashlib
import io
from pathlib import Path
import shutil
import statistics


ROOT = Path(__file__).resolve().parents[1]
CSV_FILES = {
    **{f"results/occlusion/{name}.csv": f"data/occlusion/{name}.csv"
       for name in ("summary_by_system", "summary_by_segment", "segments", "seg_test")},
    **{f"results/sutures/{name}.csv": f"data/sutures/{name}.csv"
       for name in ("stitches", "procedures", "summary", "blocks", "knot_throws",
                    "phase_times/by_system", "motion/phases", "motion/by_pig")},
    **{f"results/sutures/throws/median/{name}.csv": f"data/sutures/throws/{name}.csv"
       for name in ("knots", "by_system", "by_pig")},
    "results/sutures/throws/mode/by_system.csv": "data/sutures/throws/by_system_mode.csv",
}
FIGURES = {
    "results/occlusion/figures/occlusion_distribution.pdf": "occlusion_distribution.pdf",
    "results/occlusion/figures/occlusion_example_3mm.png": "occlusion_example_3mm.png",
    "results/occlusion/figures/occlusion_example_8mm.png": "occlusion_example_8mm.png",
    "results/sutures/figures/procedure.pdf": "procedure.pdf",
    "results/sutures/figures/overview_stats.pdf": "suture_overview.pdf",
    "results/sutures/phase_times/figures/phase_times.pdf": "suture_phase_times.pdf",
    "results/sutures/throws/median/figures/knot_throws.pdf": "knot_throws.pdf",
    "results/sutures/throws/mode/figures/knot_throws.pdf": "knot_throws_mode.pdf",
    "results/sutures/combined/suture_figure.pdf": "suture_combined.pdf",
}
REPORTS = (
    "results/sutures/sutures.md", "results/sutures/combined/suture_figure.md",
    "results/sutures/phase_times/phase_times.md", "results/occlusion/figures/figures.md",
    "scripts/suture_times.py", "scripts/occlusion_summary.py", "scripts/phase_times.py",
    "scripts/knot_throws.py", "scripts/suture_figure.py", "data/case_labels.csv",
)


def read_csv(path):
    # Accept the historical crosswalk's literal CRLF escapes as well as regular CSV.
    return list(csv.DictReader(io.StringIO(path.read_text().replace(r"\r\n", "\n"))))


def write_csv(path, fields, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def quantile(values, fraction):
    values = sorted(values)
    index = (len(values) - 1) * fraction
    lo = int(index)
    hi = min(lo + 1, len(values) - 1)
    return values[lo] + (values[hi] - values[lo]) * (index - lo)


def regenerate_summaries(source, crosswalk):
    procedures = read_csv(source / "results/sutures/procedures.csv")
    stitches = read_csv(source / "results/sutures/stitches.csv")
    expected = {r["source_recording"] for r in crosswalk if r["case_id"].startswith("P0")}
    if {r["video"] for r in procedures} != expected:
        raise ValueError("Procedure recordings do not match the seven manuscript cases")
    if {r["video"] for r in stitches} != expected:
        raise ValueError("Stitch recordings do not match the seven manuscript cases")
    cases = {r["source_recording"]: r for r in crosswalk}
    per_case = []
    for video in sorted(expected, key=lambda key: cases[key]["case_id"]):
        own = [r for r in stitches if r["video"] == video and r["failed"] == "False"]
        mean = lambda field: statistics.mean(float(r[field]) for r in own if r[field])
        end = max(float(r["cut_s"] or r["end_s"]) for r in own)
        per_case.append({
            "recording": video, "system": cases[video]["system"], "stitches": len(own),
            "mean_stitch_min": f"{mean('stitch_s') / 60:.8f}",
            "mean_gap_min": f"{mean('gap_s') / 60:.8f}",
            "suturing_span_min": f"{(end - min(float(r['start_s']) for r in own)) / 60:.8f}",
        })
    write_csv(ROOT / "data/sutures/by_pig_timing.csv", list(per_case[0]), per_case)

    summaries = []
    for system in ("3mm", "8mm"):
        own = [r for r in procedures if cases[r["video"]]["system"] == system]
        row = {"system": system, "n_cases": len(own)}
        for field in ("total_min", "dissection_min", "suturing_min"):
            values = [float(r[field]) for r in own]
            row[field + "_mean"] = f"{statistics.mean(values):.8f}"
            row[field + "_sd"] = f"{statistics.stdev(values):.8f}"
        summaries.append(row)
    write_csv(ROOT / "data/sutures/procedure_by_system.csv", list(summaries[0]), summaries)

    regions = []
    for region in ("muscle_repair", "soft_palate", "hard_palate"):
        for system in ("3mm", "8mm"):
            own = [r for r in stitches if r["block"] == region
                   and cases[r["video"]]["system"] == system and r["failed"] == "False"]
            for measure in ("stitch_s", "bite_s", "knot_s", "assistant_s"):
                available = [r for r in own if r[measure]]
                values = [float(r[measure]) for r in available]
                regions.append({
                    "region": region, "system": system, "measure": measure,
                    "pigs": len({r["video"] for r in available}), "n": len(values),
                    "q25": f"{quantile(values, .25):.8f}",
                    "median": f"{statistics.median(values):.8f}",
                    "q75": f"{quantile(values, .75):.8f}",
                })
    write_csv(ROOT / "data/sutures/region_components.csv", list(regions[0]), regions)


def manifest(source, paths, target):
    target.write_text("".join(
        f"{hashlib.sha256((source / path).read_bytes()).hexdigest()}  {path}\n"
        for path in paths
    ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT.parent / "tors-data-anal")
    parser.add_argument("--snapshot-date", required=True, help="Manifest date, YYYY-MM-DD")
    args = parser.parse_args()
    source = args.source.resolve()
    required = [*CSV_FILES, *FIGURES, *REPORTS]
    for relative in required:
        if not (source / relative).is_file():
            raise FileNotFoundError(source / relative)
    crosswalk = read_csv(ROOT / "data/case_labels.csv")
    source_cases = {r["recording_key"]: r for r in read_csv(source / "data/case_labels.csv")}
    for case in crosswalk:
        other = source_cases[case["source_recording"]]
        if (case["case_id"], case["system"]) != (other["case_id"], other["instruments"]):
            raise ValueError("Case-label mapping differs between repositories")
    for src, dst in CSV_FILES.items():
        shutil.copyfile(source / src, ROOT / dst)
    for src, dst in FIGURES.items():
        shutil.copyfile(source / src, ROOT / "figures/results" / dst)
    regenerate_summaries(source, crosswalk)
    manifest(source, [*CSV_FILES, *REPORTS], ROOT / f"data/analysis_sources_{args.snapshot_date}.sha256")
    manifest(source, FIGURES, ROOT / f"data/figure_sources_{args.snapshot_date}.sha256")
    print(f"Refreshed {len(CSV_FILES)} CSV snapshots and {len(FIGURES)} figure assets; regenerated 3 summaries.")


if __name__ == "__main__":
    main()
