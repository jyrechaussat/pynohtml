import cherrypy
from containers import (
    HtmlMaker,
    List,
    Table,
    ClassicIcon,
    Accordion,
    Paragraph
)
from fundamentals import (
    Container,
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


class Root(object):
    @pynohtml
    def index(self):
        li = List([1, 2, 3, 4])
        icon = ClassicIcon("cloud",
                           font="google",
                           klass="material-icons",
                           label="not_interested",
                           )
        tab = Table([[1, 2, 3], [1, 2, 3], [1, 2, icon]],
                    header=["A", "B", "C"],
                    tfoout=["a", "b", "c"])
        acc = Accordion({"Section 1": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        "Section 2": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        "Section 3": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        })
        mainContainer = Container([li, tab, acc])
        return mainContainer.html

    @pynohtml
    def other(self):
        l = List([1, 2, 3, 4])
        return l


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
