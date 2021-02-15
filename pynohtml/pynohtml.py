import functools
from copy import copy
import cherrypy
from pynohtml import (
    HtmlMaker,
    SpanText,
    TopNav,
    SideNav,
    Link
)
from pynohtml.fundamentals import (
    Element,
    Container,
    ImportsLibrary
)


def debug(text):
    print("#" * 100)
    print(str(text))
    print("#" * 100)


@cherrypy.expose
class pynohtml(object):
    def __init__(self, func):
        self.__self__ = None
        self.__wrapped__ = func
        self.template = func.__qualname__.split(".")[0]
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        if self.__self__ is not None:
            args = (self.__self__,) + args

        ImportsLibrary().clear()
        func_result = self.__wrapped__(*args, **kwargs)
        if isinstance(func_result, Element):
            result = func_result.html
        elif type(func_result) == str:
            result = func_result
        elif func_result is None:
            result = ""
        else:
            raise ValueError("Type not possible for pynohtml decorator")
        template = Pynohtml_core.running_templates[self.template]
        html = HtmlMaker("hello world", template(result))
        return html.html

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # create a bound copy
        bound = copy(self)
        bound.__self__ = instance

        # update __doc__ and similar attributes
        functools.update_wrapper(bound, self.__wrapped__)

        # add the bound instance to the object's dict so that
        # __get__ won't be called a 2nd time
        setattr(instance, self.__wrapped__.__name__, bound)

        return bound

    @classmethod
    def endpoints(cls, subject):
        def g():
            for name in dir(subject):
                method = getattr(subject, name)
                if isinstance(method, pynohtml):
                    yield name, method
        return [name for name, method in g()]


class Pynohtml_core:
    running_templates = {}

    def __init__(self, title, template="", endpoints=[], **kwargs):
        templates = {}
        self.template = templates.get(template, self.default_template)
        Pynohtml_core.running_templates[f"{self.__class__.__name__}"] = self.template
        self.application_title = title
        self.endpoints = pynohtml.endpoints(self)

    def default_template(self, to_include=""):
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")

        links = [buttonSideNav, Link("/", "Home")]
        for endpoint in self.endpoints:
            lo_end = endpoint.lower()
            if lo_end == "index":
                continue
            links.append(Link(f"/{lo_end}", lo_end.capitalize()))

        topnav = TopNav(links)
        sidenav = SideNav(links)
        mainContainer = Container([topnav, sidenav, to_include], id="main")
        return mainContainer


# class DecoWithArgs(object):
#     #== change the constructor's parameters to fit your needs ==
#     def __init__(self, *args):
#         self.args = args
#
#         self.__wrapped__ = None
#         self.__self__ = None
#
#     def __call__(self, *args, **kwargs):
#         if self.__wrapped__ is None:
#             return self.__wrap(*args, **kwargs)
#         else:
#             return self.__call_wrapped_function(*args, **kwargs)
#
#     def __wrap(self, func):
#         # update __doc__ and similar attributes
#         functools.update_wrapper(self, func)
#
#         return self
#
#     def __call_wrapped_function(self, *args, **kwargs):
#         # if bound to an object, pass it as the first argument
#         if self.__self__ is not None:
#             args = (self.__self__,) + args
#
#         #== change the following line to make the decorator do something ==
#         return self.__wrapped__(*args, **kwargs)
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#
#         # create a bound copy of this object
#         bound = copy(self)
#         bound.__self__ = instance
#         bound.__wrap(self.__wrapped__)
#
#         # add the bound decorator to the object's dict so that
#         # __get__ won't be called a 2nd time
#         setattr(instance, self.__wrapped__.__name__, bound)
#         return bound
#
#
