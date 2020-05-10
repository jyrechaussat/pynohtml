import os
from optparse import OptionParser
from collections import namedtuple

imports_str = """
from .fundamentals import (
    SimplestElement,
    Container,
    HeadLink
)\n\n"""


def simplestElementGenerator(configs):
    elmnts_str = """
class {X.class_name}(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("{X.tag_name}", **kwargs)\n\n"""

    result = ""
    for config in configs:
        result += elmnts_str.format(X=config)

    return result


def containerGenerator(configs):
    container_str = """
class {X.class_name}(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="{X.tag_name}",{SEP} **kwargs)\n\n"""

    result = ""
    for config in configs:
        result += container_str.format(X=config, SEP="" if config.sep == "\n" else ' sep="{}", '.format(config.sep))

    return result


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="output file path", metavar="FILE")
    (options, args) = parser.parse_args()
    output_path = options.filename

    ElementConfig = namedtuple("ElementConfig", ["class_name", "tag_name"])

    element_configs = [
        ElementConfig("Area", "area"),
        ElementConfig("Circle", "circle"),
        ElementConfig("Col", "col"),
        ElementConfig("Frame", "frame"),
        ElementConfig("Image", "img"),
        ElementConfig("LineBreak", "br"),
        ElementConfig("Meta", "meta"),
        ElementConfig("Param", "param"),
        ElementConfig("Source", "source"),
        ElementConfig("ThematicBreak", "hr"),
        ElementConfig("Track", "track"),
        ElementConfig("WordBreak", "wbr"),
    ]

    simples = simplestElementGenerator(element_configs)

    ContainerConfig = namedtuple("ContainerConfig", ["class_name", "tag_name", "sep"])

    containers_configs = [
        ContainerConfig("Abbreviation", "abbr", ""),
        ContainerConfig("Acronym", "acronym", ""),
        ContainerConfig("Address", "address", "\n"),
        ContainerConfig("Article", "article", "\n"),
        ContainerConfig("AsideText", "aside", ""),
        ContainerConfig("Audio", "audio", "\n"),
        ContainerConfig("BoldText", "b", ""),
        ContainerConfig("BdiText", "bdi", ""),
        ContainerConfig("BdoText", "bdo", ""),
        ContainerConfig("BlockQuote", "blockquote", "\n"),
        ContainerConfig("Button", "button", "\n"),
        ContainerConfig("Caption", "caption", ""),
        ContainerConfig("ColGroup", "colgroup", "\n"),
        ContainerConfig("CiteText", "cite", ""),
        ContainerConfig("CodeText", "code", ""),
        ContainerConfig("DataText", "data", ""),
        ContainerConfig("DeletedText", "del", ""),
        ContainerConfig("Details", "details", "\n"),
        ContainerConfig("DefinitionText", "dfn", ""),
        ContainerConfig("DescName", "dd", ""),
        ContainerConfig("DescTerm", "dt", ""),
        ContainerConfig("Div", "div", "\n"),
        ContainerConfig("Canvas", "canvas", ""),
        ContainerConfig("EmText", "em", ""),
        ContainerConfig("Form", "form", "\n"),
        ContainerConfig("Fieldset", "fieldset", "\n"),
        ContainerConfig("Figure", "figure", "\n"),
        ContainerConfig("Figcaption", "figcaption", "\n"),
        ContainerConfig("PageFooter", "footer", "\n"),
        ContainerConfig("PageHeader", "header", "\n"),
        ContainerConfig("ItalicText", "i", ""),
        ContainerConfig("Icon", "i", "\n"),
        ContainerConfig("InsertedText", "ins", ""),
        ContainerConfig("IFrame", "iframe", "\n"),
        ContainerConfig("Label", "label", ""),
        ContainerConfig("LegendText", "legend", ""),
        ContainerConfig("MainContent", "main", "\n"),
        ContainerConfig("Mark", "mark", ""),
        ContainerConfig("Meter", "meter", ""),
        ContainerConfig("Nav", "nav", "\n"),
        ContainerConfig("NoFrames", "noframes", ""),
        ContainerConfig("NoScript", "noscript", ""),
        ContainerConfig("Paragraph", "p", ""),
        ContainerConfig("Object", "object", ""),
        ContainerConfig("Picture", "picture", ""),
        ContainerConfig("PreformatedText", "pre", ""),
        ContainerConfig("Progress", "progress", ""),
        ContainerConfig("Quote", "q", ""),
        ContainerConfig("RubyParentheses", "rp", ""),
        ContainerConfig("RubyText", "rt", ""),
        ContainerConfig("Ruby", "ruby", ""),
        ContainerConfig("SuppressedText", "s", ""),
        ContainerConfig("Sample", "samp", ""),
        ContainerConfig("Section", "section", "\n"),
        ContainerConfig("SmallText", "small", ""),
        ContainerConfig("SpanText", "span", ""),
        ContainerConfig("RubyText", "rt", ""),
        ContainerConfig("SpanText", "span", ""),
        ContainerConfig("StrongText", "strong", ""),
        ContainerConfig("SubscriptText", "sub", ""),
        ContainerConfig("Summary", "summary", ""),
        ContainerConfig("SuperscriptText", "sup", ""),
        ContainerConfig("SvgGraphic", "svg", "\n"),
        ContainerConfig("SuperscriptText", "sup", ""),
        ContainerConfig("Template", "template", "\n"),
        ContainerConfig("TextArea", "textarea", "\n"),
        ContainerConfig("Time", "time", ""),
        ContainerConfig("Title", "title", ""),
        ContainerConfig("Time", "time", ""),
        ContainerConfig("Video", "video", "\n"),
        ContainerConfig("VarText", "var", "\n"),
    ]
    containers = containerGenerator(containers_configs)

    if output_path:
        abs_path = os.path.abspath(output_path)
        with open(abs_path, "w") as generated_file:
            generated_file.write(imports_str)
            generated_file.write(simples)
            generated_file.write(containers)
    else:
        print(imports_str)
        print(simples)
        print(containers)
