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

def debug(text):
    print("#" * 100)
    print(str(text))
    print("#" * 100)

paragraph = Paragraph("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")


class PYNOHTML_demo(Pynohtml_core):
    @pynohtml
    def index(self):
        li = List([1, 2, 3, 4])
        tab = Table([[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                    header=["A", "B", "C"],
                    tfoout=["a", "b", "c"])
        acc = Accordion({"Section 1": paragraph,
                         "Section 2": paragraph,
                         "Section 3": paragraph,
                         })
        mainContainer = Container([li, tab, acc], id="main")
        return mainContainer.html

    @pynohtml
    def uikit(self):
        card = UIKit.Card(title="My Title", inputs=paragraph)
        Uacc = UIKit.Accordion({"Section 1": paragraph,
                                "Section 2": paragraph,
                                "Section 3": [paragraph],
                                })
        alert = UIKit.Alert(Paragraph("alert with a close button"))
        no_close_alert = UIKit.Alert(Paragraph("alert with no close button"),
                                     add_close_button=False,
                                     level="warning")
        badge = UIKit.Badge(100)
        hcont = UIKit.HContainer([badge]*6)
        mainContainer = Container([card,
                                   Uacc,
                                   alert,
                                   no_close_alert,
                                   hcont,
                                   ], id="main")
        return mainContainer

    @pynohtml
    def other(self):
        para = Paragraph("hello {world}")
        mainContainer = Container([para], id="main")
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
    webapp = PYNOHTML_demo("hello world")
    cherrypy.quickstart(webapp, '/') #, conf)
