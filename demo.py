import os
import sys
import cherrypy
from pynohtml.fundamentals import Container
from pynohtml.pynohtml import Pynohtml_core, pynohtml
from pynohtml import (
    List,
    Table,
    ClassicIcon,
    Accordion,
    Paragraph,
    TopNav,
    SideNav,
    SpanText,
    Link
)
from pynohtml.elements import UIKit

paragraph = Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

icon = ClassicIcon("cloud",
                   font="google",
                   klass="material-icons",
                   label="not_interested",
                   )
li = List([1, 2, 3, 4])
tab = Table([[1, 2, 3], [1, 2, 3], [1, 2, icon]],
            header=["A", "B", "C"],
            tfoout=["a", "b", "c"])


class PYNOHTML_demo(Pynohtml_core):
    @pynohtml
    def index(self):
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")
        topnav = TopNav([buttonSideNav, Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        sidenav = SideNav([Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        acc = Accordion({"Section 1": paragraph,
                         "Section 2": paragraph,
                         "Section 3": paragraph,
                         })
        mainContainer = Container([topnav, sidenav, li, tab, acc], id="main")
        return mainContainer

    @pynohtml
    def uikit(self):
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")
        topnav = TopNav([buttonSideNav, Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        sidenav = SideNav([Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])

        card = UIKit.Card(title="My Title", inputs=paragraph)
        Uacc = UIKit.Accordion({"Section 1": paragraph,
                                "Section 2": paragraph,
                                "Section 3": [paragraph, tab],
                                })
        alert = UIKit.Alert(Paragraph("alert with a close button"))
        no_close_alert = UIKit.Alert(Paragraph("alert with no close button"), add_close_button=False, level="warning")
        badge = UIKit.Badge(100)
        hcont = UIKit.HContainer([badge]*6)
        mainContainer = Container([topnav,
                                   sidenav,
                                   card,
                                   Uacc,
                                   alert,
                                   no_close_alert,
                                   hcont,
                                   ], id="main")
        return mainContainer

    @pynohtml
    def other(self):
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")
        topnav = TopNav([buttonSideNav, Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        sidenav = SideNav([Link("/", "Home"), Link("/other", "Other"), Link("/uikit", "UIKIT")])
        para = Paragraph("hello {world}")
        mainContainer = Container([topnav, sidenav, para], id="main")
        return mainContainer

    @cherrypy.expose
    def hello(self):
        print("hello")

    def world(self):
        print("world")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 8080
    conf = {
            '/': {
                'tools.sessions.on': False,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
            },
            '/static/css': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': './static/css'},
            '/img': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': './img'},
            '/static/js': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': './static/js'},
            'global': {
                    'log.screen': True,
                    'server.socket_host': '127.0.0.1',
                    'server.socket_port': port,

            }}
    webapp = PYNOHTML_demo("hello world")
    # cherrypy.quickstart(webapp, '/') #, conf)
    print({k:v for k,v in vars(PYNOHTML_demo).items()})
    print(type(PYNOHTML_demo.other))
