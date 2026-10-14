# Transoral robotic simulated cleft palate repair

LaTeX manuscript for a **Plastic and Reconstructive Surgery, Ideas & Innovations** submission describing the laboratory's miniature 3 mm wristed instruments for simulated cleft palate repair in a **live porcine model**, compared with standard 8 mm da Vinci instruments.

## Study basis and prior work

The working study premise is [temp/premise.md](temp/premise.md). It describes **one surgeon and eight pigs, four for each instrument size**. Confirm the number of repairs/trials per animal, allocation, trial order, and protocol details from the operative records before reporting them as completed methods. No current-study outcome data have been supplied in this repository.

The supplied [Maguire et al. paper](Robotic_Assisted_Cleft_Palate_Repair_Using_Novel_3_mm_Tools_A_Reachability_and_Collision_Analysis.pdf) provides the tool design and motivation (IEEE Transactions on Biomedical Engineering, 2025;72:2085–2094; DOI: 10.1109/TBME.2025.3534119). It evaluated reachability and collisions using simulation and a synthetic cleft palate model. This manuscript concerns live porcine simulated repair and operative performance. Published simulator results must remain attributed background, not outcomes of this study.

The questions are whether the 3 mm instruments can complete the intended repair, whether immediate closure quality is comparable with 8 mm instruments, and whether miniaturization offers measurable operative advantages. These are objectives, not established findings. Smaller instruments motivate eventual applications in restricted oral workspaces; a porcine study does not establish suitability or safety for infant clinical use.

## Data and proposed measurements

Source recordings are stereo endoscopic video and robot rosbags. The premise identifies `measured_js` using cisst/CRTK definitions; inspect actual topic contents, units, timestamps, and coverage in both groups. Camera calibration is unavailable, and robot base frames are described as inaccurate.

| Domain | Proposed measures | Measurement requirements |
| --- | --- | --- |
| Feasibility | Completion of each intended step; unplanned conversion; tool failures; dropped needles; setup time | Define completion and conversion; distinguish planned manual steps; record all attempted repairs and failures. |
| Immediate closure quality | Gaps, suture spacing, bite depth | Set scoring rules and a justified comparability margin before outcome review; physical dimensions require a scale or independent measurement. These do not alone measure closure strength or healing. |
| Visualization | Fraction of image area occupied by instruments | Define the image region, mask rules, sampling, task matching, and camera-view comparability. Image fractions do not require metric stereo calibration. |
| Tissue interaction | Peak tissue force, only if a validated estimate is possible | Check joint effort/motor current and instrument calibration; account for transmission and friction. Jaw grip effort is distinct from tissue traction or needle-driving force. Otherwise report effort as a proxy. Video deformation alone is insufficient for a quantitative force claim. |
| Suturing | Time per suture, separately for nasal, muscle, and oral layers where present | Start at first needle–tissue contact; choose a consistent end at knot tightening or suture cutting; label interruptions and incomplete sutures. |
| Supporting performance | Tool–tool and tool–teeth/retractor contacts; clutch/reposition events; posterior access; grasps/regrasps; total and step time | Prespecify event definitions, exposure denominators, and rules for events outside the camera view. |
| Motion | Path length, smoothness, workspace volume | Verify kinematics, sampling, and coordinate frames. Report tool-relative workspace; do not claim anatomically registered volume from inaccurate base frames. Define any duration normalization. |

Report every computed measure, including findings favoring 8 mm instruments. Interpret lower effort or force together with task completion and closure quality; lower loading alone could reflect inadequate task execution.

## Analysis workflow

1. Inventory videos and rosbags; match files to animal, repair, instrument size, and trial order. Record missing data and incomplete repairs.
2. Synchronize video and robot clocks, check drift, and document synchronization uncertainty.
3. Annotate surgical steps, dissection intervals, sutures, layers, and events using a consistent codebook. A video annotation GUI is a possible future aid; it is not implemented here.
4. Compute per-repair measures and summarize repeated sutures by layer. Record exclusions and measurement uncertainty.
5. Use the animal/repair as the independent unit as appropriate to the confirmed design. Account for repeated sutures within repairs; do not inflate sample size using frames or sutures. With one surgeon, a surgeon random effect cannot be estimated. Emphasize descriptive comparisons and uncertainty with four pigs per group; do not claim equivalence from a nonsignificant difference.
6. Produce figures demonstrating setup, technique, visualization, and measured outcomes. Keep detailed annotation and analysis methods in supplemental material where appropriate.

Limitations to address include porcine versus infant anatomy, simulated rather than congenital defects, small sample size, one operator, learning and trial-order effects, calibration limitations, and any missing recordings. Public sharing of paired video/robot data is a possibility, subject to permissions and documentation; no dataset release is promised.

## Manuscript organization and build

- [main.tex](main.tex): manuscript metadata, inclusion of the draft, declarations, bibliography, and planned figure legends.
- [sections/draft.tex](sections/draft.tex): unstructured summary, concise presentation with integrated background, and discussion. Bracketed text identifies missing protocol details or results; no findings are invented.
- [references.bib](references.bib): bibliographic record verified from the supplied PDF; dummy examples removed.
- [prsmanuscript.cls](prsmanuscript.cls): unofficial drafting class. `journalpreview` is for internal preview; select `submission` for submission-style formatting.

Build with a TeX installation containing the class dependencies and Biber:

```sh
pdflatex main
biber main
pdflatex main
pdflatex main
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

Confirm animal characteristics, ethics protocol, simulated defect creation, platform and tool versions in both groups, allocation/order, training, anesthesia and perioperative management, camera/setup details, suture/needle specifications, intended repair steps, planned manual assistance, conversions, recording completeness, and available independent closure measurements. Add authorship, funding, disclosures, and permissions before submission.
