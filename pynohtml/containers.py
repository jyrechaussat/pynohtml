
from .fundamentals import (
	SimplestElement,
	Container,
)


class Area(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("area", **kwargs)


class Circle(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("circle", **kwargs)


class Col(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("col", **kwargs)


class Frame(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("frame", **kwargs)


class Image(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("img", **kwargs)


class LineBreak(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("br", **kwargs)


class Meta(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("meta", **kwargs)


class Param(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("param", **kwargs)


class Source(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("source", **kwargs)


class ThematicBreak(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("hr", **kwargs)


class Track(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("track", **kwargs)


class WordBreak(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("wbr", **kwargs)


class Abbreviation(Container):
    def __init__(self, abbrev=[], **kwargs):
        super().__init__(values, tag="abbr", sep="",  **kwargs)


class Acronym(Container):
    def __init__(self, acronym=[], **kwargs):
        super().__init__(values, tag="acronym", sep="",  **kwargs)


class Address(Container):
    def __init__(self, address_elmnts=[], **kwargs):
        super().__init__(values, tag="address", **kwargs)


class Article(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="article", **kwargs)


class AsideText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="aside", sep="",  **kwargs)


class Audio(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="audio", **kwargs)


class BoldText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="b", sep="",  **kwargs)


class BdiText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="bdi", sep="",  **kwargs)


class BdoText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="bdo", sep="",  **kwargs)


class BlockQuote(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="blockquote", **kwargs)


class Button(Container):
    def __init__(self, label=[], **kwargs):
        super().__init__(values, tag="button", **kwargs)


class Caption(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="caption", sep="",  **kwargs)


class ColGroup(Container):
    def __init__(self, cols=[], **kwargs):
        super().__init__(values, tag="colgroup", **kwargs)


class CiteText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="cite", sep="",  **kwargs)


class CodeText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="code", sep="",  **kwargs)


class DataText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="data", sep="",  **kwargs)


class DeletedText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="del", sep="",  **kwargs)


class Details(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="details", **kwargs)


class DefinitionText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="dfn", sep="",  **kwargs)


class DescName(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="dd", sep="",  **kwargs)


class DescTerm(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="dt", sep="",  **kwargs)


class Canvas(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="canvas", sep="",  **kwargs)


class EmText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="em", sep="",  **kwargs)


class Form(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="form", **kwargs)


class Fieldset(Container):
    def __init__(self, fields=[], **kwargs):
        super().__init__(values, tag="fieldset", **kwargs)


class Figure(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="figure", **kwargs)


class Figcaption(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="figcaption", **kwargs)


class PageFooter(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="footer", **kwargs)


class PageHeader(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="header", **kwargs)


class ItalicText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="i", sep="",  **kwargs)


class Icon(Container):
    def __init__(self, label=[], **kwargs):
        super().__init__(values, tag="i", **kwargs)


class InsertedText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="ins", sep="",  **kwargs)


class IFrame(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="iframe", **kwargs)


class Label(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="label", sep="",  **kwargs)


class LegendText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="legend", sep="",  **kwargs)


class MainContent(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="main", **kwargs)


class Mark(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="mark", sep="",  **kwargs)


class Meter(Container):
    def __init__(self, range=[], **kwargs):
        super().__init__(values, tag="meter", sep="",  **kwargs)


class Nav(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="nav", **kwargs)


class NoFrames(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="noframes", sep="",  **kwargs)


class NoScript(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="noscript", sep="",  **kwargs)


class Paragraph(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="p", sep="",  **kwargs)


class Object(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="object", sep="",  **kwargs)


class Picture(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="picture", sep="",  **kwargs)


class PreformatedText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="pre", sep="",  **kwargs)


class Progress(Container):
    def __init__(self, elments=[], **kwargs):
        super().__init__(values, tag="progress", sep="",  **kwargs)


class Quote(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="q", sep="",  **kwargs)


class RubyParentheses(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="rp", sep="",  **kwargs)


class RubyText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="rt", sep="",  **kwargs)


class Ruby(Container):
    def __init__(self, elemnts=[], **kwargs):
        super().__init__(values, tag="ruby", sep="",  **kwargs)


class SuppressedText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="s", sep="",  **kwargs)


class Sample(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="samp", sep="",  **kwargs)


class Section(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="section", **kwargs)


class SmallText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="small", sep="",  **kwargs)


class SpanText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="span", sep="",  **kwargs)


class RubyText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="rt", sep="",  **kwargs)


class SpanText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="span", sep="",  **kwargs)


class StrongText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="strong", sep="",  **kwargs)


class SubscriptText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="sub", sep="",  **kwargs)


class Summary(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="summary", sep="",  **kwargs)


class SuperscriptText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="sup", sep="",  **kwargs)


class SvgGraphic(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="svg", **kwargs)


class SuperscriptText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="sup", sep="",  **kwargs)


class Template(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="template", **kwargs)


class TextArea(Container):
    def __init__(self, initialText=[], **kwargs):
        super().__init__(values, tag="textarea", **kwargs)


class Time(Container):
    def __init__(self, datetime=[], **kwargs):
        super().__init__(values, tag="time", sep="",  **kwargs)


class Title(Container):
    def __init__(self, title=[], **kwargs):
        super().__init__(values, tag="title", sep="",  **kwargs)


class Time(Container):
    def __init__(self, datetime=[], **kwargs):
        super().__init__(values, tag="time", sep="",  **kwargs)


class Video(Container):
    def __init__(self, elmnts=[], **kwargs):
        super().__init__(values, tag="video", **kwargs)


class VarText(Container):
    def __init__(self, text=[], **kwargs):
        super().__init__(values, tag="var", **kwargs)


class Map(Container):
    def __init__(self, areas=[], **kwargs):
        if any([not isinstance(a , Area) for a in areas]):
            raise ValueError("Map argument should instance of Area")
        super().__init__(areas, tag="map", **kwargs)


class Form(Container):
    def __init__(self, elements=[], action="", method="GET", sep="\n", **kwargs):
            super().__init__(tag="form", elements=elements, action=action, method=method, sep=sep, **kwargs)


class Link(Container):
    def __init__(self, link, name, value="", **kwargs):
        super().__init__(tag = "a", elements=name, href=link, sep="", **kwargs )
        self.separator = ""


class ListElement(Container):
    def __init__(self, value, **kwargs):
        super().__init__(value, tag="li", sep="", **kwargs)


class List(Container):
    def __init__(self, l_values, ordered=False, **kwargs):
        if ordered:
            tag = "ol"
        else:
            tag = "ul"
        super().__init__(l_values, tag=tag, **kwargs)

    def processSelfList(self, l_values):
        for val in l_values:
            self.append(ListElement(val))


class DescList(Container):
    def __init__(self, values, **kwargs):
        if type(values) != dict and any([(isinstance(v, DescName) or isinstance(v, DescTerm)) for v in values]):
            raise ValueError("DescList values argument should be of dict type where keys are DescName and values are DescTerm. \nOtherWise it should be a list of DescName/DescTerm objects")
        super().__init__(l_values, tag="dl", **kwargs)

    def processSelfList(self, l_values):
        if type(l_values) == dict:
            for key, values in l_values.items():
                self.append(DescTerm(key))
                if type(values) == list:
                    for val in values:
                        self.append(DescName(val))
                else:
                    self.append(DescName(val)) 

        elif type(l_values) == list:
            self.extend(l_values)


class TableLineElement(Container):
    def __init__(self, value, isHeader=False, **kwargs):
        if isHeader:
            tag = "th"
        else:
            tag = "td"
        super().__init__(value, tag=tag, sep="", **kwargs)


class TableLine(Container):
    def __init__(self, values, tag="tr", isHeader=False, **kwargs):
        self.isHeader = isHeader
        super().__init__(values, tag=tag, **kwargs)

    def processSelfList(self, l_values):
        for val in l_values:
            self.append(TableLineElement(val, isHeader=self.isHeader))


class TableBody(Container):
    def __init__(self, l_values, tag="tbody", isHeader=False, **kwargs):
        self.isHeader = isHeader
        super().__init__(l_values, tag=tag, **kwargs)

    def processSelfList(self, l_values):
        self.append(TableLine(l_values, isHeader=self.isHeader))


class TableFooter(TableBody):
    def __init__(self, l_values, isHeader=False, **kwargs):
        super().__init__(l_values, tag="tfoot", isHeader=isHeader, **kwargs)


class TableHeader(TableBody):
    def __init__(self, l_values, isHeader=True, **kwargs):
        super().__init__(l_values, tag="thead", isHeader=isHeader, **kwargs)


class Table(Container):
    def __init__(self, 
                 table,
                 header=[],
                 tfoot=[],
                 thead=[],
                 colgroup=None,
                 caption="",
                 **kwargs):
        self.header = header
        self.caption = caption
        self.thead = thead
        self.tfoot = tfoot
        self.colgroup = colgroup
        super().__init__(table, tag="table", **kwargs)

    def processSelfList(self, l_values):
        if self.caption:
            self.append(Caption(self.caption))

        if self.colgroup and isinstance(self.colgroup, ColGroup):
            self.append(self.colgroup)

        if self.thead:
            self.append(TableHeader(self.thead))

        if self.header:
            self.append(TableLine(self.header, isHeader=True))

        for val in l_values:
            self.appendRow(val)

        if self.tfoot:
            self.append(TableFooter(self.tfoot))

    def appendRow(self, values, t_type=""):
        if isinstance(values, TableLine) or isinstance(values, TableBody):
            self.append(values)
        else:
            self.append(TableLine(values))


class Header(Container):
    def __init__(self, content, size=3, **kwargs):
        if int(size) > 6:
            size = 6
        elif int(size) < 1:
            size = 1
        self.size = size
        super().__init__(content, tag="h{}".format(size), **kwargs)


class ClassicIcon(Icon):
    def __init__(self, font, **kwargs):
        icon_fonts = {
            "google":HeadLink("https://fonts.googleapis.com/icon?family=Material+Icons"),
            "cloudfare":HeadLink("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"),
            "bootstrap":HeadLink("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css")
        }
        super().__init__(imports=icon_fonts[font], **kwargs)
