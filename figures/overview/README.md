# Procedure overview images

The editable figure is [sections/overview.tex](../../sections/overview.tex). Each card has a stage label, image path, and image-selection note. Study photographs load automatically when the matching files exist. Edit the path in the `.tex` file to use another filename or format.

| Filename | Intended view |
| --- | --- |
| `dissection.jpg` | Dissection and instrument exposure. |
| `muscle_repair.jpg` | Tool use during muscle repair. |
| `soft_palate.jpg` | Tool use during soft-palate repair. |
| `hard_palate.jpg` | Tool use during hard-palate repair. |
| `closure.jpg` | Completed closure. |
| `needle_pickup.jpg` | Needle grasp and orientation. |
| `needle_exit.jpg` | Needle emerging from tissue. |
| `knot_tightened.jpg` | Final throw tightened. |
| `assistant_cut.jpg` | Assistant cutting and removing the thread. |

- Select actual study frames. Record the case identifier, video, timestamp, instrument group, and any crop or overlay for each image.
- Keep tissue orientation and magnification comparable where feasible. Do not imply that selected images are matched if they are not.
- The current analysis starts stitch timing at first needle–tissue contact and ends it at knot tightening. The assistant interval ends at the cut annotation. Needle pickup and thread removal are proposed visual labels, not verified replacements for these numerical endpoints.
- Confirm annotation semantics before changing methods, tables, or calculated durations. No timing data were changed when this overview was added.
- Photo frames use **12:13 width:height**, matching the 960 × 1040 occlusion images. Real images are fitted without stretching; prepare a modest crop near 12:13 if needed to fill the frame. Retain uncropped source frames and document crops.
- Card width is controlled by the `\overviewstage` calls. All nine photo slots use the same display width (18% of the full figure width, capped by the card width). Photo height is calculated using the 13/12 factor in the macro; edit that factor if the intended crop changes. Labels and paths remain ordinary editable arguments.

The display uses row headings above, stage labels below unframed photographs, and small arrows. Equal-height label areas keep photographs aligned. The fourth `\overviewstage` argument is an editing note for image selection; it is not printed as a duplicate caption.
