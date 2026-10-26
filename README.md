# Transoral robotic simulated cleft palate repair

LaTeX manuscript for a **Plastic and Reconstructive Surgery, Ideas & Innovations** submission comparing miniature 3 mm wristed instruments with standard 8 mm instruments in a live porcine model.

The analysis includes seven recordings (three 3 mm, four 8 mm) from one surgeon. Visualization and timing results are drafted; repair completion, closure quality, and parts of the methods remain unfinished.

## Editing the paper

| File | Contents |
| --- | --- |
| [main.tex](main.tex) | Title, declarations, bibliography, and document options |
| [sections/draft.tex](sections/draft.tex) | Abstract, background, evaluation, and discussion |
| [sections/surgical_methods.tex](sections/surgical_methods.tex) | Animal care, operative technique, and study groups |
| [sections/procedure.tex](sections/procedure.tex), [occlusion.tex](sections/occlusion.tex), [sutures.tex](sections/sutures.tex) | Measurements, results, and figures |
| [authors.tex](authors.tex), [references.bib](references.bib) | Authors and references |
| [sections/suture_details.tex](sections/suture_details.tex), [sections/tables/](sections/tables/) | Archived analysis tables, excluded from the paper |

Bold bracketed fields mark details awaiting study records. Title-page word counts are draft estimates including placeholders. The paper contains four figures and no tables or supplementary analysis. Archived tables remain separate from the manuscript.

Citations use IEEE style (`\cite`). Use `\cref` or `\Cref` for linked figure and table references. The custom class is an unofficial drafting aid: `journalpreview` gives a two-column preview; `submission` gives manuscript formatting.

## Build

With a TeX installation including Biber, `biblatex-ieee`, and `cleveref`:

```sh
pdflatex main
biber main
pdflatex main
pdflatex main
```

Alternatively, with Tectonic and compatible Biber installed, run `make preview`. Output: `main.pdf`. `main.pdf` and LaTeX intermediates are ignored by Git.

<details>
<summary>Existing local temporary toolchain</summary>

While the tools under `/tmp` remain available:

```sh
PATH=/tmp/tors-biber:/tmp/tors-latex/bin:$PATH XDG_CACHE_HOME=/tmp/tors-tex-cache \
  make preview TECTONIC="tectonic -Z search-path=/tmp/tors-tex-extras/biblatex-ieee-1.3c"
```

</details>

## Figures and data

The four main figures are:

1. Procedure and suturing overview, edited in [sections/overview.tex](sections/overview.tex). See [photo requirements](figures/overview/README.md).
2. Procedure timelines.
3. Visual field obstruction distributions and masked examples.
4. Combined suturing times and knot throws.

Result figures in [figures/results/](figures/results/) are copied from the analysis repository, `/home/connor/tors-data-anal`; this manuscript builds independently of it. CSV snapshots are in [data/occlusion/](data/occlusion/) and [data/sutures/](data/sutures/). Dated SHA-256 manifests in [data/](data/) record provenance; the latest figure refresh is [2026-10-23](data/figure_sources_2026-10-23.sha256).

Use the fixed P01–P07 IDs from [CASE_LABELS.md](CASE_LABELS.md). Suture placement time starts at **needle pickup** and ends at final throw tightening; the subsequent interval ends at cutting, not thread removal. Repair-region annotations do not distinguish nasal and oral closure layers.

## Repository submission guidelines

These are the repository’s recorded targets; verify the journal’s current submission requirements before submission.

| Item | Limit |
| --- | --- |
| Unstructured abstract | 250 words |
| Main text | 1,000 words |
| Figures/tables | 4; confirm combined-item and panel counting |
| References | No limit recorded |
| Supplemental Digital Content | 8 items; at most 5 videos, 20 minutes total, each under 5 minutes |

The body has an innovation presentation and Discussion, without subsections. Supplementary analysis is excluded. Recount words after completing the missing content.

## Remaining work

- Complete animal-care approval, animal characteristics, anaesthesia, operative details, allocation/order, annotation methods, and synchronization.
- Verify animal-to-recording correspondence, allocation, procedure order, and operator experience against the study records.
- Verify completion, conversions, tool failures, dropped needles, and closure quality from operative records; add confirmed outcomes, funding, disclosures, prior presentation, and corresponding-author details.
- Review P01 mask quality and the final knot-to-cut exclusion, P03’s repeated repair block, and P07’s duplicate needle-through annotation.
- Finish the overview photographs and final word counts. Comparisons remain descriptive; camera position, operative differences, and the small single-surgeon sample limit interpretation.
