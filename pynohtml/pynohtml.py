import cherrypy
from containers import (
    HtmlMaker,
)
from fundamentals import (
    Element,
    ImportsLibrary
)


def pynohtml(func):
    @cherrypy.expose
    def wrapper(self):
        ImportsLibrary().clear()
        func_result = func(self)
        if isinstance(func_result, Element):
            result = func_result.html
        elif type(func_result) == str:
            result = func_result
        elif func_result is None:
            result = ""
        else:
            raise ValueError("Type not possible for pynohtml decorator")
        html = HtmlMaker("hello world", result)
        return html.html
    return wrapper
