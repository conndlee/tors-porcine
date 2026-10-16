# Transoral robotic simulated cleft palate repair

LaTeX manuscript for a **Plastic and Reconstructive Surgery, Ideas & Innovations** submission describing the laboratory's miniature 3 mm wristed instruments for simulated cleft palate repair in a **live porcine model**, compared with standard 8 mm da Vinci instruments.

## Study basis and prior work

The completed study is described in [temp/premise.md](temp/premise.md). The procedures involved **one surgeon and eight pigs, four for each instrument size**. Confirm the number of repairs/trials per animal, allocation, trial order, and protocol details from the operative records to fill in the methods. The study has been completed; its numerical results and remaining procedural details have not yet been filled into the manuscript.

The supplied [Maguire et al. paper](Robotic_Assisted_Cleft_Palate_Repair_Using_Novel_3_mm_Tools_A_Reachability_and_Collision_Analysis.pdf) provides the tool design and motivation (IEEE Transactions on Biomedical Engineering, 2025;72:2085–2094; DOI: 10.1109/TBME.2025.3534119). It evaluated reachability and collisions using simulation and a synthetic cleft palate model. This manuscript concerns live porcine simulated repair and operative performance. Published simulator results must remain attributed background, not outcomes of this study.

The study assessed completion of the intended repair, immediate closure quality relative to 8 mm instruments, and operative differences associated with miniaturization. Outcome values remain **[to be filled from the completed study]**. Smaller instruments motivate eventual applications in restricted oral workspaces; a porcine study does not establish suitability or safety for infant clinical use.

## Data and measurements

Source recordings are stereo endoscopic video and robot rosbags. The premise identifies `measured_js` using cisst/CRTK definitions; inspect actual topic contents, units, timestamps, and coverage in both groups. Camera calibration is unavailable, and robot base frames are described as inaccurate.

| Domain | Measures | Measurement requirements |
| --- | --- | --- |
| Feasibility | Completion of each intended step; conversion; tool failures; dropped needles; setup time | Define completion and conversion; distinguish protocol-specified manual steps; record all attempted repairs and failures. |
| Immediate closure quality | Gaps, suture spacing, bite depth | Document scoring rules, any comparability margin, and when they were selected; physical dimensions require a scale or independent measurement. These do not alone measure closure strength or healing. |
| Visualization | Fraction of image area occupied by instruments | Define the image region, mask rules, sampling, task matching, and camera-view comparability. Image fractions do not require metric stereo calibration. |
| Tissue interaction | Peak tissue force, only if a validated estimate is possible | Check joint effort/motor current and instrument calibration; account for transmission and friction. Jaw grip effort is distinct from tissue traction or needle-driving force. Otherwise report effort as a proxy. Video deformation alone is insufficient for a quantitative force claim. |
| Suturing | Time per suture, separately for nasal, muscle, and oral layers where present | Start at first needle–tissue contact; choose a consistent end at knot tightening or suture cutting; label interruptions and incomplete sutures. |
| Supporting performance | Tool–tool and tool–teeth/retractor contacts; clutch/reposition events; posterior access; grasps/regrasps; total and step time | Document the event definitions used, exposure denominators, and rules for events outside the camera view. |
| Motion | Path length, smoothness, workspace volume | Verify kinematics, sampling, and coordinate frames. Report tool-relative workspace; do not claim anatomically registered volume from inaccurate base frames. Define any duration normalization. |

Report every computed measure, including findings favoring 8 mm instruments. Interpret lower effort or force together with task completion and closure quality; lower loading alone could reflect inadequate task execution.

## Analysis documentation

1. **[Fill in the recording inventory and file matching]**: animal, repair, instrument size, trial order, missing data, and incomplete repairs.
2. **[Fill in synchronization details]**: clock alignment, drift checks, and timing uncertainty.
3. **[Fill in annotation details]**: surgical steps, dissection intervals, sutures, layers, event definitions, and annotation software used.
4. **[Fill in computed measures and summaries]**: per-repair values, repeated sutures by layer, exclusions, and measurement uncertainty.
5. **[Fill in statistical methods and results]**: identify the animal/repair unit used in the completed analysis. Account for repeated sutures within repairs; do not inflate sample size using frames or sutures. With one surgeon, a surgeon random effect cannot be estimated. Emphasize descriptive comparisons and uncertainty with four pigs per group; do not claim equivalence from a nonsignificant difference.
6. **[Fill in figures and supplemental material]**: setup, technique, visualization, measured outcomes, and detailed annotation/analysis methods.

Limitations to address include porcine versus infant anatomy, simulated rather than congenital defects, small sample size, one operator, learning and trial-order effects, calibration limitations, and any missing recordings. Public sharing of paired video/robot data is a possibility, subject to permissions and documentation; no dataset release is promised.

## Manuscript organization and build

- [main.tex](main.tex): manuscript metadata, inclusion of the draft, declarations, bibliography, and figure legend placeholders.
- [sections/draft.tex](sections/draft.tex): unstructured summary, concise presentation with integrated background, and discussion. Bold bracketed fields identify missing protocol details or results within manuscript prose; no findings are invented. Fill completion counts as completed/attempted repairs and report comparative values with units and uncertainty.
- [references.bib](references.bib): supplied paper plus primary studies on simulator validation, robotic simulator feasibility, and wrist friction.
- [prsmanuscript.cls](prsmanuscript.cls): unofficial drafting class. `journalpreview` is for internal preview; select `submission` for submission-style formatting.

Build with a TeX installation containing the class dependencies and Biber:

```sh
pdflatex main
biber main
pdflatex main
pdflatex main
```

For a local PDF preview with Tectonic and a compatible Biber on `PATH`, run `make preview` and open [main.pdf](main.pdf) in the editor. Tectonic downloads required TeX packages on its first run and runs the bibliography processor automatically. The generated `main.pdf`, LaTeX intermediates, and local `build/` and `out/` directories are ignored by Git so they stay out of the Overleaf sync. Manuscript sources, reference PDFs, and figure assets remain eligible for Git.

The rendered preview includes the bibliography, red WIP headings, and bold placeholders. The temporary toolchain (Tectonic with Biber 2.17 for its bundled biblatex 3.17) used in this session is under `/tmp` and may disappear after a restart. While it exists, rebuild using:

```sh
PATH=/tmp/tors-biber:/tmp/tors-latex/bin:$PATH XDG_CACHE_HOME=/tmp/tors-tex-cache make preview
```

Verify actual abstract and body word counts after completing the draft; title-page counts remain placeholders.

## Repository submission guidelines

The original README records the following Ideas & Innovations limits; confirm against the journal's instructions before submission:

- Unstructured summary/abstract: **250 words** maximum.
- Main text: **1,000 words** maximum.
- References: **no limit** recorded.
- Figures/tables: **4** recorded; verify how combined items and panels are counted.
- Supplemental Digital Content: **8 items** total, including at most **5 video clips**, up to **20 minutes total**, each clip **under 5 minutes**.

The manuscript should summarize the authors' experience and highlight the technique or innovation, with high-quality illustrations or videos showing its application. The category is not intended as a miniature Original Article. Use an unstructured summary, a concise presentation answering **what** the innovation is (**no subheadings/subsections**), and a discussion explaining **why** it matters. Demographic and outcome data may be requested by editors or reviewers.

## Details still needed

Confirm animal characteristics, ethics protocol, simulated defect creation, platform and tool versions in both groups, allocation/order, training, anesthesia and perioperative management, camera/setup details, suture/needle specifications, intended repair steps, protocol-specified manual assistance, conversions, recording completeness, and available independent closure measurements. Add authorship, funding, disclosures, and permissions before submission.

## Draft headings and source checks

Red headings marked **WIP** identify unfinished sections. The subsection headings are drafting aids; remove them from the concise presentation for submission, as required by the repository guidelines. Bold bracketed fields identify missing details and numerical results.

Sources traced from the supplied PDF and checked against primary-study records:

- [Podolsky et al., 2017: simulator validation](https://pubmed.ncbi.nlm.nih.gov/28027241/) — background on the synthetic platform.
- [Podolsky et al., 2017: robotic simulator feasibility](https://pubmed.ncbi.nlm.nih.gov/28121879/) — wrist articulation, visualization, and instrument-size constraints.
- [Ho et al., 2024: wrist friction](https://theiccilab.com/2024/11/characterization-of-friction-within-a-novel-3-mm-wristed-robotic-instrument/) — pitch-dependent friction relevant to interpreting logged effort.

Wu et al.'s 2020 instrument paper (DOI: 10.1109/TMRB.2020.2977737), cited in the supplied PDF, is an additional lead. Its primary full text was not accessible during this pass; no new claims were attributed to it.

## Occlusion results

[sections/occlusion.tex](sections/occlusion.tex) is included through the main draft and contains segmentation test performance and a whole-recording occlusion table for six videos (two 3 mm, four 8 mm). The source repository `/home/connor/tors-data-anal` was accessed read-only. Its `plans/visual_field.md` documents the measure; numerical results came from `results/occlusion/seg_test.csv` and `data/derived/occlusion/video/*.parquet`, checked against the segmentation and inference scripts.

Small numerical snapshots are retained in [data/occlusion](data/occlusion): the test CSV, per-video summary CSV, and SHA-256 hashes of source outputs. No external repository is needed to compile the manuscript. Percentages in the table were computed from the parquet values before rounding. These are whole-recording descriptive results, not step-matched or suturing-only comparisons. The six recordings require reconciliation with the eight-animal study description. Camera distance varied; one tool-free test frame produced a false positive, and the segmentation test split was within recordings. No between-group significance or equivalence is asserted.

The occlusion table adds an item to the four existing figure placeholders; reconcile the final selection with the four-item figure/table allowance. Recheck the main-text word limit when merging the completed results into the concise presentation.
