import os
from .fundamentals import (
    Element,
    Container,
)

from .containers import Link


class SideNav(Container):
    def __init__(self, links=[]):
        super().__init__(elements=links, klass="sidenav", id="PyNoHtmlSideNav")
        self.addCSS(fromFile="sidenav.css")
        self.addJs(fromFile="sidenav.js")

    def processSelfList(self, l_values):
        self.append(Link("javascript:void(0)",
                         "&times;",
                         klass="closebtn",
                         onclick="closeNav()"))
        for val in l_values:
            if isinstance(val, Element):
                self.append(val)
            else:
                self.append(Link(val))

class TopNav(Container):
    def __init__(self, links=[]):
        super().__init__(elements=links, klass="topnav", id="myTopnav")
        self.addCSS(fromFile="topnav.css")

    def processSelfList(self, l_values):
        for val in l_values:
            if isinstance(val, Element):
                self.append(val)
            else:
                self.append(Link(val))
