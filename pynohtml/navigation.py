from .fundamentals import (
Element,
Container,
)
from .containers import Link 

# from .fundamentals import debugprint

class SideNav(Container):
    def __init__(self, links=[]):
        super().__init__(elements=links, klass="sidenav", id="PyNoHtmlSideNav")

        self.addHLink("./static/css/sidenav.css")

        self.addJs("""

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("PyNoHtmlSideNav").style.width = "150px";
  document.getElementById("main").style.marginLeft = "150px";
  document.getElementById("openclosebutton").onclick=closeNav;
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("PyNoHtmlSideNav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("openclosebutton").onclick=openNav;
}
""")

    def processSelfList(self, l_values):
        self.append(Link("javascript:void(0)", "&times;", klass="closebtn", onclick="closeNav()" ))
        for val in l_values:
            if isinstance(val, Element):
                self.append(val)
            else:
                self.append(Link(val))

class TopNav(Container):
    def __init__(self, links=[]):
        super().__init__(elements=links, klass="topnav", id="myTopnav")
        self.addHLink("./static/css/topnav.css")

    def processSelfList(self, l_values):
        for val in l_values:
            if isinstance(val, Element):
                self.append(val)
            else:
                self.append(Link(val))
