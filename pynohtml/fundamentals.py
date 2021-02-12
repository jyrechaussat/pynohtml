class ImportsLibrary:
    class __ImportsLibrary(set):
        def addImports(self, imports):
            for imp in imports:
                if not isinstance(imp, Import):
                    raise ValueError("Can't add other than Import type into ImportLibrary")
                self.add(imp)

    instance = None

    def __init__(self):
        if not ImportsLibrary.instance:
            ImportsLibrary.instance = ImportsLibrary.__ImportsLibrary()

    def __len__(self):
        return len(ImportsLibrary.instance)

    def append(self, imports):
        if type(imports) == list:
            raise ValueError("type list not accepted for append method, please use extend")
        ImportsLibrary.instance.addImports([imports])

    def extend(self, imports):
        if type(imports) not in (set, list):
            raise ValueError("type other than list or set not accepted for extend method, please use append")
        ImportsLibrary.instance.addImports(imports)

    def clear(self):
        ImportsLibrary.instance.clear()

    @property
    def importsInHead(self):
        return [imp for imp in ImportsLibrary.instance if imp.inHead]

    @property
    def importsInBody(self):
        return [imp for imp in ImportsLibrary.instance if not imp.inHead]


class Element:
    def __init__(self, klass="", **kwargs):
        self.imports = ImportsLibrary()
        self.css_dict = kwargs
        if klass:
            self.css_dict["class"] = klass

    def processCss(self):
        css = ""
        for key, value in self.css_dict.items():
            if type(value) == bool:
                if value:
                    css += f" {key}"
            else:
                css += f' {key}="{value}"'
        return css

    @property
    def html(self):
        return "<element{self.css}>"


class SimpleElement(Element):
    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag

    @property
    def html(self):
        css = self.processCss()
        return f"<{self.tag}{css}>"


class Container(list, Element):
    def __init__(self, elements=[], tag="div", sep="\n", **kwargs):
        if type(elements) == list:
            list.__init__(self, elements)
        else:
            list.__init__(self, [elements])
        Element.__init__(self, **kwargs)
        self.tag = tag
        self.sep = sep

    def make(self):
        return self

    def processElements(self):
        elmts = self.make()
        result = ""
        if elmts:
            result += self.sep
            for elmt in elmts:
                if isinstance(elmt, Element):
                    result += elmt.html
                else:
                    result += str(elmt)
                result += self.sep
        return result

    @property
    def html(self):
        css = self.processCss()
        data = self.processElements()
        return f"<{self.tag}{css}>" + data + f"</{self.tag}>"


class Import(Element):
    def __init__(self, data, inHead=True, isLink=False, tag="script", sep='\n', **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.hashed_data = hash(data)
        self.tag = tag
        self.sep = sep
        self.inHead = inHead
        self.isLink = isLink

    def __hash__(self):
        return self.hashed_data

    def __eq__(self, other):
        if isinstance(other, Import):
            return self.data == other.data
        elif type(other) == str:
            return self.data == other
        return False

    @property
    def html(self):
        css = self.processCss()
        if self.isLink:
            result = f"<{self.tag}{css}>"
        else:
            result = f"<{self.tag}{css}>" + self.sep + self.data + self.sep + f"</{self.tag}>"
        return result


class HeadLink(Import):
    def __init__(self, link, rel="stylesheet", **kwargs):
        super().__init__(link, tag="link", isLink=True, rel=rel, href=link, **kwargs)


class Script(Import):
    def __init__(self, src, **kwargs):
        super().__init__("", tag="script", sep="", src=src)
        self.hashed_data = hash(src)


class BodyScript(Import):
    def __init__(self, script, **kwargs):
        super().__init__(script, src=script, inHead=False, tag="script", **kwargs)


class Javascript(Import):
    def __init__(self, script, **kwargs):
        super().__init__(script, tag="script", inHead=False, type="text/javascript", **kwargs)


class Style(Import):
    def __init__(self, style, **kwargs):
        super().__init__(style, tag="style", **kwargs)


class Base(Import):
    def __init__(self, src, target="_blank", **kwargs):
        super().__init__(src, tag="base", href=src, target=target, isLink=True, **kwargs)
