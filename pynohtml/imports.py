from fundamentals import Import


class HeadLink(Import):
    isLink = True
    def __init__(self, link, rel="stylesheet", **kwargs):
        super().__init__(link, tag="link", rel=rel, href=link, **kwargs)


class Script(Import):
    isLink = True
    def __init__(self, src):
        super().__init__("", tag="script", sep="", src=src)


class BodyScript(Import):
    inHead = False
    def __init__(self, script):
        super().__init__(script, tag="script")

class Javascript(Import):
    inHead = False
    def __init__(self, script):
        super().__init__(script, tag="script", type="text/javascript")


class Style(Import):
    def __init__(self, style):
        super().__init__(style, tag="style")


class CSSStyle(Import):
    def __init__(self, style):
        super().__init__(style, tag="style", type="text/css")


class Base(Import):
    def __init__(self, src, target="_blank", **kwargs):
        super().__init__("", tag="base", href=src, target=target, **kwargs)