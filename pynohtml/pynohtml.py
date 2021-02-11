import cherrypy
from elements import *
from root import (
    Container,
    Element,
    ImportsLibrary
)



def pynohtml(func):
    @cherrypy.expose
    def wrapper(self):
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


class Root(object):
    @cherrypy.expose
    def index(self):
        l = List([1, 2, 3, 4])
        return l.html

    @pynohtml
    def other(self):
        l = List([1, 2, 3, 4])
        return l

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
    # r = Root()
    # print(r.other())
