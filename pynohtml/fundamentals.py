from pynohtml.imports import (
    Script,
    Javascript,
    CSSStyle,
    Style,
    HeadLink
)


def debugprint(data):
    print("#" * 40)
    print(data)
    print("#" * 40)


class Element(object):
    def __init__(self, klass="", imports=[], **kwargs):
        self.base_html = ""
        self.css_dict = kwargs
        self.css = ""
        if type(imports) != list:
            self.imports = [imports]
        else:
            self.imports = imports
        self.klass = klass

    def processCss(self):
        self.css = ""
        if self.klass:
            self.css += " "
            if self.klass:
                self.css += 'class="{KLASS}"'.format(KLASS=self.klass)

        if self.css_dict:
            for key, value in self.css_dict.items():
                self.css += " "
                if type(value) == bool:
                    self.css += key
                else:
                    self.css += '{K}="{V}"'.format(K=key, V=value)

    def addScript(self, imp ):
        self.imports.append(Script(imp))

    def addHLink(self, link):
        self.imports.append(HeadLink(link))

    def addJs(self, js):
        self.imports.append(Javascript(js))

    def addCSS(self, css):
        self.imports.append(CSSStyle(css))

    def addStyle(self, style):
        self.imports.append(Style(style))

    def getImports(self):
        return self.imports

    def postProcess(self):
        pass

    def __str__(self):
        self.postProcess()
        self.processCss()
        return self.base_html.format(X=self)


class SimplestElement(Element):
    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.base_html = "<{X.tag}{X.css}>"


class Container(list, Element):
    def __init__(self, elements=[], tag="div", sep="\n", **kwargs):
        list.__init__(self, [])
        Element.__init__(self, **kwargs)
        if type(elements) not in [list, dict]:
            elements = [elements]
        self.processSelfList(elements)
        self.tag = tag
        self.sep = sep

    def getImports(self):
        result = []
        for element in list(self):
            if isinstance(element, Element):
                result.extend(element.getImports())
        result.extend(self.imports)
        return result

    def processSelfList(self, l_values):
        self.extend(l_values)

    def postProcess(self):
        return self.sep.join([str(element) for element in list(self)])

    def __str__(self):
        self.processCss()
        self.base_html = "<{X.tag} {X.css}>{X.sep}"
        self.base_html += self.postProcess()
        self.base_html += "{X.sep}</{X.tag}>"
        return self.base_html.format(X=self)
