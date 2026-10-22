# Figure priorities and a four-figure layout

**Selected layout:** The PDF now includes the top four available figures: occlusion, full procedure, per-suture phase timing, and knot throws. The stitch-overview figure has been removed from the PDF. Its per-pig statistics are preserved in an editable LaTeX table, [sections/tables/suture_by_pig.tex](sections/tables/suture_by_pig.tex). All tables are collected in the draft supplement, leaving four main display items. The technique-focused layout below remains an alternative for a later writing pass.

“Significance” below means relevance to the paper's argument. These descriptive results do not establish statistical significance or equivalence.

## Ranking the available figures

| Rank | Figure | Importance and supported message | Main limitation | Recommendation |
| --- | --- | --- | --- | --- |
| 1 | [Occlusion distribution and masked views](figures/results/occlusion_distribution.pdf) | This is the clearest measured advantage associated with the 3 mm instruments. Recording-level median obstruction was 10.39% versus 23.93%. The images make the metric tangible. | Camera position and task mix differed. The distribution pools frames; its medians differ from the case-level summaries. | Retain as a three-panel figure: distribution and one masked view per instrument size. |
| 2 | [Full procedure timeline](figures/results/procedure.pdf) | This shows the complete annotated workflow, including dissection, repair phases, pauses, and elapsed time. It puts the favorable visualization result alongside the longer procedure times. | Procedures differed in stitch count and annotated phases. The May 29 endpoint excludes the final assistant interval. | Retain; pair with phase timing if a slot is needed for the technique. |
| 3 | [Per-suture phase timing](figures/results/suture_phase_times.pdf) | This separates needle passage, knot tying, and assistant time. Individual points expose skew and outliers that group averages conceal. | Stitches are clustered within pigs. The plot alone does not identify why the groups differed. | Retain, either alone or below the procedure timeline. |
| 4 | [Knot throws: mode version](figures/results/knot_throws_mode.pdf) | This adds context to knot duration: three throws was the most common count in both groups. Timing-density peaks were 39.4 versus 40.2 seconds per counted throw. | Similar peaks do not establish equivalent performance. Peaks depend on smoothing, and the timed interval includes thread pull-through. | Retain if knot construction is a central point; otherwise this is the first main figure to move to the supplement. |
| 5 | [Stitch overview with per-pig statistics](figures/results/suture_overview.pdf) | This preserves sequence, gaps, assistant intervals, and case-level variation. | Much of its message overlaps the full procedure and phase-timing figures. It is dense at reduced size. | Remove from the PDF; retain its per-pig statistics in the native LaTeX table. The source graphic remains available. |

## Recommended layout for an Ideas & Innovations paper

Reserve space for showing the actual technique. The existing result plots explain performance, but none fully demonstrates instrument setup, defect creation, or layered repair.

| Final figure | Panels | Content and purpose | Asset status |
| --- | --- | --- | --- |
| **1. Instruments and repair technique** | A–C | A: 3 mm and 8 mm instruments with scale. B: porcine transoral setup. C: representative repair sequence or completed closure, with essential labels. | Appropriate study images still need selection. Closure imagery illustrates the procedure; it does not establish measured closure quality. |
| **2. Instrument occlusion** | A–C | A: occlusion distribution. B: selected 3 mm masked view. C: selected 8 mm masked view. | All assets exist. Keep the illustrative views explicitly unmatched for camera position. |
| **3. Procedure and per-suture timing** | A–D | A: full procedure timeline across seven recordings. B: needle-passage duration. C: knot-tying duration. D: assistant interval. | Both source figures exist. Use the procedure timeline across the top and the three phase panels in one row below. |
| **4. Knot construction and timing** | A–B | A: throws per knot. B: knot interval per counted throw, with density-mode markers. | The existing two-panel mode figure already provides this layout. |

This gives four numbered figures. Figure 3 requires composition and relabelling; placing two existing PDFs side by side would make their labels too small. Keep the procedure rows legible and use a common purple/teal instrument palette where appropriate. The procedure-phase colors represent anatomy or workflow, not instrument groups.

If the combined timing figure is too dense at publication size, move the knot figure to the supplement and give the full procedure and per-suture timing separate main-figure slots. The technique and occlusion figures remain the first two.

## Four figures using only the assets available now

Until technique images are selected, a complete results-only layout is:

1. **Occlusion:** the distribution and two masked views.
2. **Full procedure:** dissection, repair phases, and elapsed time.
3. **Per-suture timing:** the existing three phase panels.
4. **Knot throws:** the existing count and time-mode panels.

This layout is implemented. The stitch overview is replaced by an editable supplemental table; five numbered figures become four without shrinking panels. It fits the available results, although the technique-focused layout above better serves the article category.

## Supplemental material and tables

- Keep the stitch-overview statistics in the editable supplemental table. Individual-case timelines remain supplemental candidates; consolidate related cases where practical.
- Keep detailed repair-region, phase-motion, and workspace tables in the supplement. Motion has only two 3 mm pigs with rosbags, so it is weaker support for the main comparison.
- All tables, including the former main summary tables, are now collected in the draft supplement. Essential numerical results remain in the main text and figure legends.
- Use one knot figure version in the main paper. The median and mode versions show the same underlying observations and do not warrant separate main slots. Medians can remain in a supplemental table.
- Do not promote the preliminary insertion-effort preview to a tissue-force figure without validation.

## Checks for the writing and assembly pass

- The user-specified limit is four figures; the README records four **figures/tables**. The conservative layout is four numbered figures with all tables supplemental. Panel-count acceptance still needs confirmation from the journal instructions; grouping panels alone does not establish compliance.
- Keep recording counts, stitch counts, and exclusions explicit. Distinguish case-level summaries, pooled stitch summaries, and pooled frame distributions.
- Distinguish density modes from medians. Do not describe the 39.4 versus 40.2 second peaks as proof of equivalence.
- Show the timing disadvantage alongside the visualization advantage. Avoid a general claim that smaller instruments were faster or more efficient.
- Keep the technique-image slot conditional on selecting suitable study images. Do not substitute prior simulator photographs as evidence of the porcine procedure.
