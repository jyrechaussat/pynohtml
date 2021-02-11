from .fundamentals import (
    Element,
)

from .containers import (
    Div,
    SpanText
)

from .navigation import (
    SideNav
)


class Importations(set):
    def __init__(self, firstAdd):
        self.html = ""
        self.type = None
        self.inHead = False
        self.isLink = False
        self.append(firstAdd)

    def append(self, toadd):
        if len(self) == 0:
            self.inHead = toadd.inHead
            self.isLink = toadd.isLink
            if not toadd.isLink:
                self.html = str(toadd)
        self.add(toadd)

    def __str__(self):
        result = ""
        if self.isLink:
            result = "\n".join([str(x) for x in self])
        else:
            l_imports = "\n".join([x.data for x in self])
            result = self.html.format(DATA=l_imports)
        return result


class HtmlMaker(list, Element):
    def __init__(self, title, sep="\n"):
        list.__init__(self)
        Element.__init__(self)
        self.base_html = """<!DOCTYPE html>
<head>
{X.title_html}
{X.head_imports}
</head>
<body>
{X.body_html}
</br>
{X.body_imports}
</body>
</html>"""
        self.sep = sep
        self.title = title

    def postProcess(self):
        self.title_html = ""
        if self.title:
            self.title_html = "<title>{X.title}</title>".format(X=self)

        self.body_html = self.processBody()

    def processStylesAndScripts(self):
        imports_def = {}
        for element in self:
            for imp in element.getIncludes():
                if type(imp) not in imports_def.keys():
                    imports_def[type(imp)] = Importations(imp)
                else:
                    imports_def[type(imp)].append(imp)

        self.head_imports = "\n".join([str(I) for k, I in imports_def.items() if I.inHead])
        self.body_imports = "\n".join([str(I) for k, I in imports_def.items() if not I.inHead])

    def processBody(self):
        self.processStylesAndScripts()
        return self.sep.join([str(element) for element in list(self)])


class MailMaker(Container):
    def __ini__(self, elements=[]):
        super().__init__(elements, tag="html")


class PynohtmlPage:
    def __init__(self):
        self.htmlmaker = HtmlMaker("")
        self.page = Div(id="main")

    def clear(self):
        self.page.clear()

    def append(self, element):
        self.page.append(element)

    def generate(self):
        result = str(self.maker)
        self.clear()
        return result


class SideNavPage(PynohtmlPage):
    def __init__(self, title, links, toggle="", fixed=False):
        self.maker = HtmlMaker(title)
        sideNav = SideNav(links, fixed=fixed)
        self.maker.addCSS(fromFile="sidenav.css")
        self.maker.append(sideNav)
        if not toggle:
            toggle = SpanText("&#9776; {TITLE}".format(TITLE=title),
                              id="openclosebutton",
                              onclick="openNav()",
                              style="font-size:30px;cursor:pointer")

        self.all = Div(id="main")
        self.all.append(toggle)
        self.page = Div(id="dynamic")
        self.all.append(self.page)
        self.maker.append(self.all)
