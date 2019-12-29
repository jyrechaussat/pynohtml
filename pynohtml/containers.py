from .fundamentals import (
    Element,
    SimplestElement,
    Container,
)

from .imports import (
    Style,
    CSSStyle,
    Script,
    Javascript
)


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

