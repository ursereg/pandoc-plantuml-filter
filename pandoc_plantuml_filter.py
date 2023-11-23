"""
Pandoc filter using panflute
"""

import os, subprocess, hashlib
import panflute as pf


PLANTUML_BIN = os.environ.get("PLANTUML_BIN", "plantuml")
PLANTUML_DIR = os.environ.get("PLANTUML_DIR", "plantuml-images")


def prepare(doc: pf.elements.Doc):
    try:
        os.mkdir(PLANTUML_DIR)
    except FileExistsError:
        pass


def generate(block: pf.CodeBlock, filetype="svg") -> str:
    txt = block.text
    filename = f"plantuml-images/{hashlib.sha1(txt.encode()).hexdigest()}"
    src = filename + ".uml"
    dest = filename + "." + filetype
    if not os.path.isfile(dest):
        with open(src, "wb") as f:
            f.write(txt.encode())
        subprocess.check_call(PLANTUML_BIN.split() + ["-t" + filetype, src])
    return dest


def action(element, doc):
    if isinstance(element, pf.CodeBlock) and "plantuml" in element.classes:
        img_path = generate(element)
        img_caption = element.attributes.get("caption", "")
        image = pf.Image(
            pf.Str(img_caption),
            url=img_path,
            title=img_caption,
            attributes=element.attributes,
        )
        caption = None
        if "caption" in element.attributes:
            caption = pf.Caption(pf.Plain(pf.Str(img_caption)))
            return pf.Figure(
                pf.Plain(image), caption=caption, identifier=element.identifier
            )
        return pf.Para(image)


def main(doc=None):
    return pf.run_filter(action, prepare=prepare, doc=doc)


if __name__ == "__main__":
    main()
