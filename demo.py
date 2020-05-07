import os
import sys
import cherrypy
import inspect

from pynohtml.htmlmaker import HtmlMaker

from pynohtml.fundamentals import (
    Container,
    Script,
)
from pynohtml.containers import (
    Div,
    Header,
    ClassicIcon,
    Link,
    Image,
    Paragraph,
    Accordion,
    CodeText,
    BoldText,
    Table
)

from pynohtml.navigation import (
    TopNav,
    SideNav,
)


class PYNOHTML_demo:
    def generate(self, pageDiv):
        maker = HtmlMaker("maker")
        icon = Div(ClassicIcon(font="google",
                               klass="material-icons",
                               label="not_interested",
                               style="font-size:60px;color:lightblue;text-shadow:2px 2px 4px #000000;"),
                               id="openclosebutton",
                               onclick="openNav()"
                               )
        sideLinks = [Link("./index", name="Welcome"),
                     Link("./simpleExamples", name="Samples"),
                     Link("./DataTable", name="DataTable"),
                    ]


        sidenav = SideNav(sideLinks)
        top = TopNav(links=[icon, Link("/", "Home")])
        cont = Div(top)
        cont.append(sidenav)
        mainDiv = Div(elmnts=pageDiv, id="main", style="background-color:#5D5D5D")
        maker.append(cont)
        maker.append(mainDiv)
        return str(maker)

    @cherrypy.expose
    def index(self):
        container = Div(id="pres")
        container.append(Header("PYNOHTML Documentation"))
        container.append(Paragraph("This website is the demo page of what you can do with pynohtml python package"))
        return self.generate(container)


    @cherrypy.expose
    def simpleExamples(self):
        bold = BoldText("bold text")
        sentence = "Here is a paragraph with {BOLD} in the center".format(BOLD=str(bold))
        print("#" * 100)
        print(sentence)
        print("#" * 100)
        code = inspect.getsource(PYNOHTML_demo.simpleExamples)
        elmnts = [Header("Simple HTML Elements"),
                  Header("Headers with size 4", size=4),
                  Header("Headers with size 3", size=3),
                  Header("Headers with size 2", size=2),
                  Header("Headers with size 1", size=1),
                  Header("Paragraph", size=1),
                  Paragraph("bnjviroe"),
                  Accordion("Code", code)
                  ]
        container = Div(elmnts, id="pres")
        return self.generate(container)
     
    @cherrypy.expose
    def DataTable(self):
        icon = Div(ClassicIcon(font="google",
                               klass="material-icons",
                               label="house",
                               style="font-size:60px;color:lightblue;text-shadow:2px 2px 4px #000000;"),
                               id="openclosebutton",
                               onclick="openNav()"
                               )


        table = [[1,3,4,5,6],
                 ["Str1", "Str2", "Str3", Paragraph("a paragraph object"), icon],
                 [Table([[1,2,3],[1,2,3],[1,2,3]]),1,2,3,4]
                 ]

        htmlTable = Table(table) 
        cont = Div(htmlTable)
        return self.generate(cont)


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
   # Configure server and port

   cherrypy.quickstart(webapp, '/', conf)
