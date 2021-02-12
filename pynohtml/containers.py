from fundamentals import (
    SimpleElement,
    Container,
    ImportsLibrary,
    HeadLink
)


class Head(Container):
    def __init__(self, title, inputs=[], **kwargs):
        self.title = title
        super().__init__(elements=inputs, tag="head", **kwargs)

    def make(self):
        result = [Title(self.title)]
        il = ImportsLibrary()
        result.extend(il.importsInHead)
        return result


class Body(Container):
    def __init__(self, body_elemts, **kwargs):
        super().__init__(elements=body_elemts, tag="body", **kwargs)

    def make(self):
        result = [elmt for elmt in self]
        il = ImportsLibrary()
        result.extend(il.importsInBody)
        return result


class HtmlMaker(Container):
    def __init__(self, title, main_containers, lang="en"):
        self.title = title
        self.body = main_containers
        super().__init__(tag="html", lang=lang)

    def make(self):
        result =  [DocType(),
                Meta(charset="utf-8"),
                Head(self.title),
                Body(self.body)]
        return result


class Area(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("area", **kwargs)


class Circle(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("circle", **kwargs)


class Col(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("col", **kwargs)


class DocType(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("!doctype", html=True)


class Frame(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("frame", **kwargs)


class Image(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("img", **kwargs)


class LineBreak(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("br", **kwargs)


class Meta(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("meta", **kwargs)


class Param(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("param", **kwargs)


class Source(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("source", **kwargs)


class ThematicBreak(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("hr", **kwargs)


class Track(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("track", **kwargs)


class WordBreak(SimpleElement):
    def __init__(self, **kwargs):
        super().__init__("wbr", **kwargs)


class Abbreviation(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="abbr", sep="",  **kwargs)


class Acronym(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="acronym", sep="",  **kwargs)


class Address(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="address", **kwargs)


class Article(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="article", **kwargs)


class AsideText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="aside", sep="",  **kwargs)


class Audio(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="audio", **kwargs)


class BoldText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="b", sep="",  **kwargs)


class BdiText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="bdi", sep="",  **kwargs)


class BdoText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="bdo", sep="",  **kwargs)


class BlockQuote(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="blockquote", **kwargs)


class Button(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="button", **kwargs)


class Caption(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="caption", sep="",  **kwargs)


class ColGroup(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="colgroup", **kwargs)


class CiteText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="cite", sep="",  **kwargs)


class CodeText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="code", sep="",  **kwargs)


class DataText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="data", sep="",  **kwargs)


class DeletedText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="del", sep="",  **kwargs)


class Details(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="details", **kwargs)


class DefinitionText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="dfn", sep="",  **kwargs)


class Div(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="div", **kwargs)


class Canvas(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="canvas", sep="",  **kwargs)


class EmText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="em", sep="",  **kwargs)


class Form(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="form", **kwargs)


class Fieldset(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="fieldset", **kwargs)


class Figure(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="figure", **kwargs)


class Figcaption(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="figcaption", **kwargs)


class PageFooter(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="footer", **kwargs)


class PageHeader(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="header", **kwargs)


class ItalicText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="i", sep="",  **kwargs)


class Icon(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="i", **kwargs)


class InsertedText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="ins", sep="",  **kwargs)


class IFrame(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="iframe", **kwargs)


class Label(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="label", sep="",  **kwargs)


class LegendText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="legend", sep="",  **kwargs)


class MainContent(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="main", **kwargs)


class Mark(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="mark", sep="",  **kwargs)


class Meter(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="meter", sep="",  **kwargs)


class Nav(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="nav", **kwargs)


class NoFrames(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="noframes", sep="",  **kwargs)


class NoScript(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="noscript", sep="",  **kwargs)


class Paragraph(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="p", sep="",  **kwargs)


class Object(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="object", sep="",  **kwargs)


class Picture(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="picture", sep="",  **kwargs)


class PreformatedText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="pre", sep="",  **kwargs)


class Progress(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="progress", sep="",  **kwargs)


class Quote(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="q", sep="",  **kwargs)


class RubyParentheses(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="rp", sep="",  **kwargs)


class RubyText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="rt", sep="",  **kwargs)


class Ruby(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="ruby", sep="",  **kwargs)


class SuppressedText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="s", sep="",  **kwargs)


class Sample(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="samp", sep="",  **kwargs)


class Section(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="section", **kwargs)


class SmallText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="small", sep="",  **kwargs)


class SpanText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="span", sep="",  **kwargs)


class StrongText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="strong", sep="",  **kwargs)


class SubscriptText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="sub", sep="",  **kwargs)


class Summary(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="summary", sep="",  **kwargs)


class SuperscriptText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="sup", sep="",  **kwargs)


class SvgGraphic(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="svg", **kwargs)


class Template(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="template", **kwargs)


class TextArea(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="textarea", **kwargs)


class Time(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="time", sep="",  **kwargs)


class Title(Container):
    def __init__(self, title, **kwargs):
        super().__init__(elements=[title], tag="title", sep="",  **kwargs)


class Video(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="video", **kwargs)


class VarText(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="var", **kwargs)


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


class Header(Container):
    def __init__(self, content, size=3, **kwargs):
        if int(size) > 6:
            size = 6
        elif int(size) < 1:
            size = 1
        self.size = size
        super().__init__(content, tag="h{}".format(size), **kwargs)


class ListElement(Container):
    def __init__(self, value, **kwargs):
        super().__init__(elements=value, tag="li", sep="", **kwargs)


class List(Container):
    def __init__(self, values, ordered=False, **kwargs):
        if ordered:
            tag = "ol"
        else:
            tag = "ul"
        super().__init__(values, tag=tag, **kwargs)

    def make(self):
        return [elmt if isinstance(elmt, ListElement) else ListElement(elmt) for elmt in self]


class DescName(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="dd", sep="",  **kwargs)


class DescTerm(Container):
    def __init__(self, inputs=[], **kwargs):
        super().__init__(elements=inputs, tag="dt", sep="",  **kwargs)


class DescList(Container):
    def __init__(self, values, **kwargs):
        if type(values) != dict \
           and any([(isinstance(v, DescName) or isinstance(v, DescTerm)) for v in values]):
            raise ValueError("DescList values argument should be of dict type where keys are DescName and values are DescTerm. \nOtherWise it should be a list of DescName/DescTerm objects")
        self.values = values
        super().__init__(tag="dl", **kwargs)

    def make(self):
        result = []
        if type(self.values) == dict:
            for key, values in self.values.items():
                result.append(DescTerm(key))
                if type(values) == list:
                    for val in values:
                        result.append(DescName(val))
                else:
                    result.append(DescName(val))

        elif type(self.values) == list:
            result.extend(self.values)
        else:
            raise ValueError("Do not understand the type of DescList Input")

        return result


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

    def make(self):
        return [TableLineElement(elmt, isHeader=self.isHeader) for elmt in self]


class TableBody(Container):
    def __init__(self, values, tag="tbody", isHeader=False, **kwargs):
        self.isHeader = isHeader
        super().__init__(values, tag=tag, **kwargs)

    def make(self):
        return [TableLine([x for x in self], isHeader=self.isHeader)]


class TableFooter(TableBody):
    def __init__(self, values, isHeader=False, **kwargs):
        super().__init__(values, tag="tfoot", isHeader=isHeader, **kwargs)


class TableHeader(TableBody):
    def __init__(self, values, isHeader=True, **kwargs):
        super().__init__(values, tag="thead", isHeader=isHeader, **kwargs)


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

    def make(self):
        if self.caption:
            self.append(Caption(self.caption))

        if self.colgroup and isinstance(self.colgroup, ColGroup):
            self.append(self.colgroup)

        if self.thead:
            self.append(TableHeader(self.thead))

        if self.header:
            self.append(TableLine(self.header, isHeader=True))

        for val in self:
            self.appendRow(val)

        if self.tfoot:
            self.append(TableFooter(self.tfoot))

    def appendRow(self, values):
        if isinstance(values, TableLine) or isinstance(values, TableBody):
            self.append(values)
        else:
            self.append(TableLine(values))


class ClassicIcon(Icon):
    def __init__(self, value="", font="google", **kwargs):
        icon_fonts = {
            "google":HeadLink("https://fonts.googleapis.com/icon?family=Material+Icons"),
            "cloudfare":HeadLink("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"),
            "bootstrap":HeadLink("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css")
        }
        super().__init__(value, **kwargs)
        self.imports.append(icon_fonts[font])


