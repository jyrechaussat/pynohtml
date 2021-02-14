import os
import sys
import cherrypy
from containers import (
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


class PYNOHTML_demo:
    @pynohtml
    def index(self):
        icon = ClassicIcon("cloud",
                           font="google",
                           klass="material-icons",
                           label="not_interested",
                           )
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")
        topnav = TopNav([buttonSideNav, Link("/", "Home"), Link("/other", "Other")])
        sidenav = SideNav([Link("/", "Home"), Link("/other", "Other")])
        li = List([1, 2, 3, 4])
        tab = Table([[1, 2, 3], [1, 2, 3], [1, 2, icon]],
                    header=["A", "B", "C"],
                    tfoout=["a", "b", "c"])
        acc = Accordion({"Section 1": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        "Section 2": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        "Section 3": Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
                        })
        mainContainer = Container([topnav, sidenav, li, tab, acc], id="main")
        return mainContainer

    @pynohtml
    def other(self):
        buttonSideNav = SpanText("&#9776;open",
                                 style="font-size:30px;cursor:pointer",
                                 id="openclosebutton",
                                 onclick="openNav()")
        topnav = TopNav([buttonSideNav,
                         Link("/", "Home"),
                         Link("/other", "Other")])
        sidenav = SideNav([Link("/", "Home"), Link("/other", "Other")])
        para = Paragraph("hello {world}")
        mainContainer = Container([topnav, sidenav, para], id="main")
        return mainContainer


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
    webapp = PYNOHTML_demo()
    cherrypy.quickstart(webapp, '/') #, conf)
