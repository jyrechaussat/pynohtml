def debugprint(data):
    print("#" * 40)
    print(data)
    print("#" * 40)


class Element(object):
    def __init__(self, klass="", includes=[], **kwargs):
        self.base_html = ""
        self.css_dict = kwargs
        self.css = ""
        if type(includes) != list:
            self.includes = [includes]
        else:
            self.includes = includes
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

    def addScript(self, imp, **kwargs):
        self.includes.append(Script(imp, **kwargs))

    def addHLink(self, link, **kwargs):
        self.includes.append(HeadLink(link, **kwargs))

    def addJs(self, js, **kwargs):
        self.includes.append(Javascript(js, **kwargs))

    def addCSS(self, css, **kwargs):
        self.includes.append(CSSStyle(css, **kwargs))

    def addStyle(self, style, **kwargs):
        self.includes.append(Style(style, **kwargs))

    def addBodyScript(self, src):
        self.includes.append(BodyScript(src=src))

    def getIncludes(self):
        return self.includes

    def postProcess(self):
        pass

    def __repr__(self):
        return str(self)

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
        self.make()
        self.tag = tag
        self.sep = sep

    def getIncludes(self):
        result = []
        for element in list(self):
            if isinstance(element, Element):
                result.extend(element.getIncludes())
        result.extend(self.includes)
        return result

    def processSelfList(self, l_values):
        self.extend(l_values)

    def make(self):
        pass

    def postProcess(self):
        return self.sep.join([str(element) for element in list(self)])

    def __repr__(self):
        return str(self)

    def __str__(self):
        self.processCss()
        self.base_html = "<{X.tag} {X.css}>{X.sep}"
        self.base_html += self.postProcess()
        self.base_html += "{X.sep}</{X.tag}>"
        return self.base_html.format(X=self)


class Include(Element):
    inHead = True
    isLink = False

    def __init__(self, data, tag="script", sep="\n", **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.tag = tag
        self.sep = sep
        if self.isLink:
            self.base_html = "<{X.tag} {X.css}>{X.sep}</{X.tag}>"
        else:
            self.base_html = "<{X.tag} {X.css}>{{DATA}}</{X.tag}>{X.sep}"

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        if isinstance(other, Include):
            return self.data == other.data
        elif type(other) == str:
            return self.data == other
        return False


class HeadLink(Include):
    isLink = True

    def __init__(self, link, rel="stylesheet", **kwargs):
        super().__init__(link, tag="link", rel=rel, href=link, **kwargs)


class Script(Include):
    isLink = True

    def __init__(self, src, **kwargs):
        super().__init__("", tag="script", sep="", src=src)


class BodyScript(Include):
    inHead = False

    def __init__(self, script="", **kwargs):
        super().__init__(script, tag="script", **kwargs)


class Javascript(Include):
    inHead = False

    def __init__(self, script, **kwargs):
        super().__init__(script, tag="script", type="text/javascript", **kwargs)


class Style(Include):
    def __init__(self, style, **kwargs):
        super().__init__(style, tag="style", **kwargs)


class CSSStyle(Include):
    def __init__(self, style, **kwargs):
        super().__init__(style, tag="style", type="text/css", **kwargs)


class Base(Include):
    def __init__(self, src, target="_blank", **kwargs):
        super().__init__("", tag="base", href=src, target=target, **kwargs)
