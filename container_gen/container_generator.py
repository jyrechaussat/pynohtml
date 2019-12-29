import os
import sys
from optparse import OptionParser
from collections import namedtuple

imports_str = """
from kitchen.cockery import (
	SimplestElement,
	Container,
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
    def __init__(self, {X.values_name}=[], **kwargs):
        super().__init__(values, tag="{X.tag_name}",{SEP} **kwargs)\n\n"""

	result = ""
	for config in configs:
		result += container_str.format(X=config, SEP= "" if config.sep == "\n" else ' sep="{}", '.format(config.sep))

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

	ContainerConfig = namedtuple("ContainerConfig", ["class_name", "tag_name", "values_name", "sep"])
	
	containers_configs = [
		ContainerConfig("Abbreviation", "abbr", "abbrev", ""),
		ContainerConfig("Acronym", "acronym", "acronym", ""),
		ContainerConfig("Address", "address", "address_elmnts", "\n"),
		ContainerConfig("Article", "article", "elmnts", "\n"),
		ContainerConfig("AsideText", "aside", "text", ""),
		ContainerConfig("Audio", "audio", "elmnts", "\n"),
		ContainerConfig("BoldText", "b", "text", ""),
		ContainerConfig("BdiText", "bdi", "text", ""),
		ContainerConfig("BdoText", "bdo", "text", ""),
		ContainerConfig("BlockQuote", "blockquote", "elmnts", "\n"),
		ContainerConfig("Button", "button", "label", "\n"),
		ContainerConfig("Caption", "caption", "text", ""),
		ContainerConfig("ColGroup", "colgroup", "cols", "\n"),
		ContainerConfig("CiteText", "cite", "text", ""),
		ContainerConfig("CodeText", "code", "text", ""),
		ContainerConfig("DataText", "data", "text", ""),
		ContainerConfig("DeletedText", "del", "text", ""),
		ContainerConfig("Details", "details", "elmnts", "\n"),
		ContainerConfig("DefinitionText", "dfn", "text", ""),
		ContainerConfig("DescName", "dd", "text", ""),
		ContainerConfig("DescTerm", "dt", "text", ""),
		ContainerConfig("Canvas", "canvas", "elmnts", ""),
		ContainerConfig("EmText", "em", "text", ""),
		ContainerConfig("Form", "form", "elmnts", "\n"),
		ContainerConfig("Fieldset", "fieldset", "fields", "\n"),
		ContainerConfig("Figure", "figure", "elmnts", "\n"),
		ContainerConfig("Figcaption", "figcaption", "elmnts", "\n"),
		ContainerConfig("PageFooter", "footer", "elmnts", "\n"),
		ContainerConfig("PageHeader", "header", "elmnts", "\n"),
		ContainerConfig("ItalicText", "i", "text", ""),
		ContainerConfig("Icon", "i", "label", "\n"),
		ContainerConfig("InsertedText", "ins", "text", ""),
		ContainerConfig("IFrame", "iframe", "elmnts", "\n"),
		ContainerConfig("Label", "label", "text", ""),
		ContainerConfig("LegendText", "legend", "text", ""),
		ContainerConfig("MainContent", "main", "elmnts", "\n"),
		ContainerConfig("Mark", "mark", "text", ""),
		ContainerConfig("Meter", "meter", "range", ""),
		ContainerConfig("Nav", "nav", "elmnts", "\n"),
		ContainerConfig("NoFrames", "noframes", "text", ""),
		ContainerConfig("NoScript", "noscript", "text", ""),
		ContainerConfig("Paragraph", "p", "text", ""),
		ContainerConfig("Object", "object", "elmnts", ""),
		ContainerConfig("Picture", "picture", "elmnts", ""),
		ContainerConfig("PreformatedText", "pre", "text", ""),
		ContainerConfig("Progress", "progress", "elments", ""),
		ContainerConfig("Quote", "q", "text", ""),
		ContainerConfig("RubyParentheses", "rp", "text", ""),
		ContainerConfig("RubyText", "rt", "text", ""),
		ContainerConfig("Ruby", "ruby", "elemnts", ""),
		ContainerConfig("SuppressedText", "s", "text", ""),
		ContainerConfig("Sample", "samp", "text", ""),
		ContainerConfig("Section", "section", "elmnts", "\n"),
		ContainerConfig("SmallText", "small", "text", ""),
		ContainerConfig("SpanText", "span", "text", ""),
		ContainerConfig("RubyText", "rt", "text", ""),
		ContainerConfig("SpanText", "span", "text", ""),
		ContainerConfig("StrongText", "strong", "text", ""),
		ContainerConfig("SubscriptText", "sub", "text", ""),
		ContainerConfig("Summary", "summary", "text", ""),
		ContainerConfig("SuperscriptText", "sup", "text", ""),
		ContainerConfig("SvgGraphic", "svg", "elmnts", "\n"),
		ContainerConfig("SuperscriptText", "sup", "text", ""),
		ContainerConfig("Template", "template", "elmnts", "\n"),
		ContainerConfig("TextArea", "textarea", "initialText", "\n"),
		ContainerConfig("Time", "time", "datetime", ""),
		ContainerConfig("Title", "title", "title", ""),
		ContainerConfig("Time", "time", "datetime", ""),
		ContainerConfig("Video", "video", "elmnts", "\n"),
		ContainerConfig("VarText", "var", "text", "\n"),
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