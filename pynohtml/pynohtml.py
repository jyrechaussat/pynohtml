import cherrypy
from pynohtml import (
    HtmlMaker,
)
from pynohtml.fundamentals import (
    Element,
    ImportsLibrary
)


# def pynohtml(func):
#     @cherrypy.expose
#     def wrapper(self):
#         ImportsLibrary().clear()
#         func_result = func(self)
#         if isinstance(func_result, Element):
#             result = func_result.html
#         elif type(func_result) == str:
#             result = func_result
#         elif func_result is None:
#             result = ""
#         else:
#             raise ValueError("Type not possible for pynohtml decorator")
#         html = HtmlMaker("hello world", result)
#         return html.html
#     return wrapper


class pynohtml:
    def __init__(self, method):
        self._method = method

    @cherrypy.expose
    def __call__(self, obj, *args, **kwargs):
        ImportsLibrary().clear()
        func_result = self._method(obj, *args, **kwargs)
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

    @classmethod
    def endpoints(cls, subject):
        def g():
            for name in dir(subject):
                method = getattr(subject, name)
                if isinstance(method, pynohtml):
                    yield name, method
        return [name for name, method in g()]

class Pynohtml_core:
    def __init__(self, title, template="", endpoints=[], **kwargs):
        templates = {}
        self.template = templates.get(template, HtmlMaker)
        self.application_title = title
        print(self.default_template())

    def default_template(self, to_include=""):
        endpoints = pynohtml.endpoints(self)
        print("#" * 100)
        print(endpoints)
        print("#" * 100)
        # buttonSideNav = SpanText("&#9776;open",
        #                          style="font-size:30px;cursor:pointer",
        #                          id="openclosebutton",
        #                          onclick="openNav()")
        # topnav = TopNav([buttonSideNav, Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        # sidenav = SideNav([Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        # mainContainer = Container([topnav, sidenav, to_indlue], id="main")
        return ""



