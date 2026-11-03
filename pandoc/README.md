# Word export

From the repository root:

```sh
make word
```

Output: `pandoc/build/manuscript.docx`. Requires Python 3, Pandoc, Tectonic, and `pdftoppm` (Poppler). Pandoc processes the manuscript and bibliography; Tectonic renders the four figure layouts as images.

To also compile the LaTeX PDF, run `./scripts/build.sh` from the repository root (or `make all`).

All conversion scripts, citation styles, and generated files stay in this folder. The LaTeX sources remain authoritative. Word uses 12-point Times New Roman, double-spaced body text, one-inch margins, and continuous line numbers. Figures retain editable captions and linked references; verification text remains red. Word pagination differs from the PDF, and citations are formatted text rather than reference-manager fields.

Executable overrides:

```sh
make word PANDOC=/path/to/pandoc TECTONIC=/path/to/tectonic
# Or invoke the converter directly:
python3 pandoc/export.py --output /tmp/manuscript.docx
```

The bundled [IEEE CSL style](https://github.com/citation-style-language/styles/blob/master/ieee.csl) is distributed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/); attribution and license details are in `ieee.csl`.
