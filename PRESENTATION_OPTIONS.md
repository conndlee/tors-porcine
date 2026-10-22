# Case labels, section order, and display layout

## Selected case labels

The manuscript uses **P01–P07**, assigned chronologically to the seven main cases, and **Pilot** for the excluded mixed-instrument case. [CASE_LABELS.md](CASE_LABELS.md) records the fixed crosswalk and the analysis-repository update instruction; [data/case_labels.csv](data/case_labels.csv) is the machine-readable mapping. Regenerated figure exports have been imported, including the P01–P07 procedure labels.

## Earlier case-label options

| Option | Example | Advantages | Tradeoff |
| --- | --- | --- | --- |
| **Neutral case IDs (recommended)** | P01--P07 | Compact and formal; keeps calendar dates out of plot labels. The label stays fixed if group assignments or display order change. | Needs a stable link to source files. IDs must not silently change between figures or revisions. |
| Letters | Case A--G | Short labels work well in figures. | Letters can be confused with subfigure panels A--D. They do not explain whether their order is chronological. |
| Group-coded IDs | 3mm-01--03; 8mm-01--04 | Instrument group is immediately visible. | Embeds a group assignment in the identifier and makes the mixed-instrument pilot awkward. |
| Calendar dates | May 29; June 15 | Directly traceable to the analysis outputs; sequence is visible. | Adds calendar detail that contributes little to the main clinical message. |

Use **P01--P07** for the seven main cases and a separate pilot ID. Retain a local source-file crosswalk. If IDs follow chronological order, say so; if they do not, provide procedure order separately. A label is not evidence that a recording corresponds to a unique animal: confirm the animal log first.

- Suggested display order: group cases by instrument size and keep procedure order within each group.
- Report assignment, order, and operator familiarization in the design description. Discuss learning effects in the limitations.
- Do not use relabelling to obscure the sequence or imply randomization. Omitting calendar dates is a presentation choice, not anonymization of a repository that already contains dated source files.
- **Current decision:** P01–P07 follow chronological main-case order; Pilot is separate. Source recording keys remain unchanged. No source-analysis files were modified.

## Section-order options

**Option A: procedure, then visibility, then detailed suturing (implemented).**

1. Background and repair technique.
2. Operative evaluation and full annotated procedure (Figure 1).
3. Instrument occlusion (Figure 2).
4. Individual-suture timing and knot throws (Figures 3 and 4).
5. Discussion and limitations.

This introduces what was done before describing the view and task-level performance. Occlusion is the second result subsection rather than the opening result.

**Option B: keep all timing results together.** Present full procedure, individual sutures, and knot throws, followed by occlusion. This creates a single performance sequence, but puts the visualization advantage later and does not make it the second result subsection.

**Option C: separate technique from measured performance.** Lead with technique/closure images, then procedure and suturing, then occlusion. This suits the innovation category once suitable technique images are selected; it requires revisiting the four-figure selection.

## Width and flow trial

- Figure 1 remains a full-width, top-of-page procedure timeline. It is an exception because seven cases and several phases need horizontal space.
- Occlusion uses one column: distribution above the two example frames.
- Per-suture timing uses vertically stacked source panels in one column. Vector crops preserve the source text and data; the original PDF remains unchanged.
- Knot throws uses vertically stacked count and time-density panels in one column.
- Tables use one-column layouts. Wide comparisons are reorganized into separate phase panels or measure rows rather than reduced to unreadably small type.
- The draft supplement uses two-column pages as well, with each table confined to a column. Tables remain separate editable `.tex` files.

Inspect the preview at actual publication width. A tall phase-timing figure can occupy most of a column; this is preferable to making its three horizontal panels too small to read. Top-of-page float placement can move a figure beyond its first text citation, so references and numbered captions remain essential.

## Combined timing/throws revision

The quantitative phase-timing and knot-throw plots now form one single-column three-panel Figure 4. A draft procedure/suture-event schematic is the headliner (Figure 1), followed by full-procedure timelines (Figure 2) and occlusion (Figure 3). The combined plot is exported at single-column size from the analysis repository; phase durations share panel a, followed by throw counts (b) and time per throw (c). The selected case labels are P01–P07 and Pilot.
