#!/usr/bin/env python3
"""Export the manuscript to Word without changing its LaTeX sources."""

import argparse
from pathlib import Path
import re
import shlex
import shutil
import struct
import subprocess
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
ET.register_namespace("w", W)
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")


def run(command, **kwargs):
    return subprocess.run(command, check=True, **kwargs)


def uncomment(text):
    # A TeX comment consumes its end-of-line too; preserving it adds spaces
    # between tightly packed minipages and can wrap an entire figure panel.
    return re.sub(r"(?<!\\)%[^\n]*(?:\n|$)", "", text)


def group(text, start):
    while text[start].isspace():
        start += 1
    if text[start] != "{":
        raise ValueError(f"Expected braced argument near {text[start:start+60]!r}")
    depth = 1
    end = start + 1
    while depth:
        if text[end] == "{" and text[end - 1] != "\\":
            depth += 1
        elif text[end] == "}" and text[end - 1] != "\\":
            depth -= 1
        end += 1
    return text[start + 1:end - 1], end


def replace_command(text, name, count, callback):
    pattern = re.compile(r"\\" + name + r"(?![A-Za-z])")
    result, cursor = [], 0
    for match in pattern.finditer(text):
        if match.start() < cursor:
            continue
        args, end = [], match.end()
        for _ in range(count):
            arg, end = group(text, end)
            args.append(arg)
        result.extend([text[cursor:match.start()], callback(*args)])
        cursor = end
    return "".join(result) + text[cursor:]


def value(text, name):
    match = re.search(r"\\" + name + r"(?![A-Za-z])", text)
    return group(text, match.end())[0]


def expand(path, stack=()):
    path = path.resolve()
    if path in stack:
        raise ValueError(f"Circular input: {path}")
    text = uncomment(path.read_text())
    return replace_command(text, "input", 1, lambda p: expand(
        ROOT / (p if Path(p).suffix else p + ".tex"), (*stack, path)))


def reference_doc(pandoc, output):
    """Start with Pandoc's styles; apply the manuscript's submission layout."""
    default = run([pandoc, "--print-default-data-file=reference.docx"],
                  stdout=subprocess.PIPE).stdout
    original = output.with_suffix(".default.docx")
    original.write_bytes(default)
    def tag(name):
        return f"{{{W}}}{name}"
    def child(parent, name, **attrs):
        node = parent.find(tag(name))
        if node is None:
            node = ET.SubElement(parent, tag(name))
        for key, val in attrs.items():
            node.set(tag(key), str(val))
        return node
    with zipfile.ZipFile(original) as source, zipfile.ZipFile(output, "w") as target:
        for item in source.infolist():
            data = source.read(item.filename)
            if item.filename == "word/styles.xml":
                tree = ET.fromstring(data)
                defaults = child(tree, "docDefaults")
                props = child(child(defaults, "rPrDefault"), "rPr")
                child(props, "rFonts", ascii="Times New Roman", hAnsi="Times New Roman")
                child(props, "sz", val=24)
                child(child(child(defaults, "pPrDefault"), "pPr"), "spacing",
                      line=480, lineRule="auto", after=0)
                verification = ET.SubElement(tree, tag("style"),
                                             {tag("type"): "character", tag("styleId"): "Verification"})
                child(verification, "name", val="Verification")
                child(child(verification, "rPr"), "color", val="FF0000")
                for style in tree.findall(tag("style")):
                    sid = style.get(tag("styleId"))
                    if sid in {"Normal", "BodyText", "FirstParagraph", "Bibliography"}:
                        child(child(style, "pPr"), "spacing", line=480, lineRule="auto", after=0)
                    if sid in {"Title", "Subtitle", "Heading1", "Heading2", "Caption", "ImageCaption"}:
                        props = child(style, "rPr")
                        child(props, "rFonts", ascii="Times New Roman", hAnsi="Times New Roman")
                        child(props, "sz", val=24)
                        child(props, "color", val="000000")
                    if sid == "Hyperlink":
                        child(child(style, "rPr"), "color", val="4D9BC8")
                    if sid in {"Caption", "ImageCaption"}:
                        child(child(style, "rPr"), "i", val=0)
                        props = child(style, "pPr")
                        child(props, "spacing", line=240, lineRule="auto", after=120)
                        child(props, "keepLines")
                data = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
            elif item.filename == "word/document.xml":
                tree = ET.fromstring(data)
                for section in tree.iter(tag("sectPr")):
                    child(section, "pgSz", w=12240, h=15840)
                    child(section, "pgMar", top=1440, bottom=1440, left=1440, right=1440)
                    child(section, "lnNumType", countBy=1, restart="continuous", distance=360)
                data = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
            target.writestr(item, data)
    original.unlink()


def keep_figures_together(path):
    """Keep each image paragraph with its following caption in Word."""
    temporary = path.with_suffix(".tmp.docx")
    with zipfile.ZipFile(path) as source, zipfile.ZipFile(temporary, "w") as target:
        for item in source.infolist():
            data = source.read(item.filename)
            if item.filename == "word/document.xml":
                tree = ET.fromstring(data)
                for paragraph in tree.iter(f"{{{W}}}p"):
                    if paragraph.find(f".//{{{W}}}drawing") is not None:
                        props = paragraph.find(f"{{{W}}}pPr")
                        if props is None:
                            props = ET.Element(f"{{{W}}}pPr")
                            paragraph.insert(0, props)
                        ET.SubElement(props, f"{{{W}}}keepNext")
                        ET.SubElement(props, f"{{{W}}}jc", {f"{{{W}}}val": "center"})
                data = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
            target.writestr(item, data)
    temporary.replace(path)


def artwork(body, number, build, tectonic):
    """Typeset exactly the artwork body, on a page sized to its TeX box."""
    name = f"figure-{number}"
    body = body.replace("{figures/", "{" + str(ROOT / "figures") + "/")
    source = build / f"{name}.tex"
    source.write_text(r"""\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{newtxtext,newtxmath,graphicx,xcolor,duckuments}
\pagestyle{empty}
\begin{document}
\hoffset=-1in\voffset=-1in
\setbox0=\vbox{\hsize=6.5in\linewidth=6.5in\textwidth=6.5in
""" + body + r"""\par}
\shipout\vbox{\special{papersize=\the\wd0,\the\dimexpr\ht0+\dp0\relax}\box0}
\end{document}
""")
    log = build / f"{name}.log.txt"
    try:
        with log.open("w") as stream:
            run([*tectonic, "--outdir", str(build), str(source)], cwd=ROOT,
                stdout=stream, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        raise SystemExit(f"Figure {number} failed to render; see {log}")
    run(["pdftoppm", "-singlefile", "-r", "220", "-png",
         str(build / f"{name}.pdf"), str(build / name)], stdout=subprocess.DEVNULL)
    image = build / f"{name}.png"
    width, height = struct.unpack(">II", image.read_bytes()[16:24])
    inches = min(6.5, 7.0 * width / height)
    return image, inches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pandoc", default="pandoc")
    parser.add_argument("--tectonic", default="tectonic", help="Executable and optional Tectonic flags")
    parser.add_argument("--output", type=Path, default=HERE / "build/manuscript.docx")
    args = parser.parse_args()
    tectonic = shlex.split(args.tectonic)
    for executable in [args.pandoc, tectonic[0], "pdftoppm"]:
        if not shutil.which(executable):
            parser.error(f"Missing executable: {executable}. See pandoc/README.md.")
    output = args.output.resolve()
    build = HERE / "build"
    build.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    source = expand(ROOT / "main.tex")
    title = value(source, "PRStitle")
    front = ("\\section*{" + title + "}\n" + value(source, "PRSauthors") + "\n\n"
             + value(source, "PRSaffiliations") + "\n\n"
             + r"\textbf{Correspondence:} " + value(source, "PRScorrespondence")
             + "\n\n" + value(source, "PRSmetadata") + "\n\n")
    text = source.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    text = text.replace(r"\PRSmaketitle", front)
    labels = {}
    figures = []
    def figure(body, caption, aliases):
        number = len(figures) + 1
        primary = aliases.split(",")[0].strip()
        for label in aliases.split(","):
            labels[label.strip()] = (primary, number)
        figures.append((body, caption))
        image, width = artwork(body, number, build, tectonic)
        # Pandoc retains the label as a Word bookmark and the caption as text.
        return ("\n\\begin{figure}\n"
                + f"\\includegraphics[width={width:.4f}in]{{{image}}}\n"
                + f"\\caption{{{caption}}}\\label{{{primary}}}\n\\end{{figure}}\n")
    text = re.sub(r"\\begin\{figure\*?\}(?:\[[^\]]*\])?", "", text)
    text = re.sub(r"\\end\{figure\*?\}", "", text)
    text = replace_command(text, "PRSfigurecontent", 3, figure)
    text = text.replace(r"\begin{PRSabstract}", r"\section*{Abstract}")
    text = text.replace(r"\end{PRSabstract}", "").replace(r"\PRSstartbody", "")
    text = replace_command(text, "PRSkeywords", 1, lambda s: r"\par\textbf{Keywords:} " + s + "\n\n")
    text = replace_command(text, "PRSdisclosure", 2, lambda a,b: r"\par\textbf{" + a + ":} " + b + "\n\n")
    text = replace_command(text, "verifytext", 1, lambda s: r"\textcolor{red}{" + s + "}")
    def ref(match):
        primary, number = labels[match[2]]
        prefix = "Figure" if match[1] == "Cref" else "Fig."
        return f"\\href{{#{primary}}}{{{prefix} {number}}}"
    text = re.sub(r"\\(Cref|cref)\{([^}]+)\}", ref, text)
    text = re.sub(r"\\hyperref\[([^]]+)\]", lambda m: "\\href{#" + labels[m[1]][0] + "}", text)
    text = re.sub(r"\\printbibliography(?:\[[^]]*\])?", "", text)
    prepared = build / "manuscript.tex"
    prepared.write_text(text)
    reference = build / "reference.docx"
    reference_doc(args.pandoc, reference)
    run([args.pandoc, str(prepared), "--from=latex", "--to=docx", "--standalone",
         "--citeproc", "--bibliography", str(ROOT / "references.bib"),
         "--csl", str(HERE / "ieee.csl"), "--reference-doc", str(reference),
         "--metadata=reference-section-title:References", "--metadata=link-citations:true",
         "--lua-filter", str(HERE / "word.lua"), "--output", str(output)], cwd=ROOT)
    keep_figures_together(output)
    print(f"Created {output} ({len(figures)} figures)")


if __name__ == "__main__":
    main()
