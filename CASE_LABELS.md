# Case labels

The manuscript uses P01–P07 in chronological order of the seven main cases. The excluded mixed-instrument case is labelled Pilot. IDs are fixed across analyses, figures, and revisions; source recording keys remain unchanged. The mapping is also stored in [data/case_labels.csv](data/case_labels.csv).

| Case ID | Source date | Instruments | Source recording key |
| --- | --- | --- | --- |
| P01 | 2026-05-29 | 3mm | `pig_may29-2026-05-29_09.34.18` |
| P02 | 2026-06-15 | 3mm | `pig_jun15-2026-06-15_10.14.18` |
| P03 | 2026-06-16 | 3mm | `pig_jun16-2026-06-16_09.57.53` |
| P04 | 2026-08-18 | 8mm | `pig_aug18-2026-08-18_10.10.14` |
| P05 | 2026-08-19 | 8mm | `pig_aug19-2026-08-19_12.09.17` |
| P06 | 2026-10-07 | 8mm | `pig_oct07-2026-10-07_14.31.12` |
| P07 | 2026-10-08 | 8mm | `pig_oct08-2026-10-08_13.19.52` |
| Pilot | 2026-05-28 | mixed | `pig_may28-2026-05-28_10.17.17` |

## Instruction for the analysis repository

Copy the following instruction into the analysis-repository session, together with the mapping above (or `data/case_labels.csv`):

> Adopt the manuscript's fixed case-label crosswalk: P01 = May 29, P02 = June 15, P03 = June 16, P04 = August 18, P05 = August 19, P06 = October 7, and P07 = October 8 (all 2026). Label the mixed-instrument May 28 case Pilot and keep it excluded from the main comparison. Use the exact source recording keys in the crosswalk to resolve cases, rather than assigning IDs from a filtered dataset's row order.
>
> Put the mapping in one shared configuration or helper and use it for every figure title, tick label, legend entry, annotation, generated caption, and result table that identifies an individual case. Cover occlusion, full-procedure timelines, per-case suture plots, phase timing, throws, motion, and combined figures, including supplementary and preview outputs. Display P01–P07 in numeric order within instrument groups. Keep instrument size as a separate attribute; the mapping is fixed if a subset is plotted or groups are reordered.
>
> Preserve raw data, dated source filenames, recording keys, timestamps, analysis values, exclusions, and existing output paths used by the manuscript. This is a display-label change. Keep source dates and keys in the crosswalk for traceability. Use case IDs in generated reporting prose, including the P01 assistant-interval exclusion, P03 repeated block, and P07 duplicate annotation.
>
> Regenerate all affected PDF and PNG figures and accompanying Markdown reports from the plotting scripts, including `results/sutures/figures/procedure.pdf` and `results/sutures/combined/suture_figure.pdf`. Check that every source case resolves to the expected ID, that Pilot remains separate, that no calendar labels remain in publication-facing output, and that numerical results are unchanged. Report the changed output paths so the manuscript copies can be refreshed.

The regenerated figure exports were imported on October 22, 2026. The copied procedure timeline uses P01–P07; all copied result PDFs were checked for dated case labels. Source hashes are recorded in [data/figure_label_sources_2026-10-22.sha256](data/figure_label_sources_2026-10-22.sha256). The case IDs are presentation labels tied to source recordings; they do not independently verify the animal-to-recording correspondence.
