from .fundamentals import (
    Element,
    Container,
)

from .containers import Link


class SideNav(Container):
    def __init__(self, links=[]):
        super().__init__(elements=links, klass="sidenav", id="PyNoHtmlSideNav")

        self.addCSS("""
/* The side navigation menu */
.sidenav {
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  top: 40;
  left: 0;
  background-color: #424242; /* Black*/
  border-right-style: solid;
  border-width: 3px;
  border-color: #111;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 10px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
}

/* The navigation menu links */
.sidenav a {
  padding: 8px 4px 8px 8px;
  text-decoration: none;
  font-size: 15px;
  color: #F280FE;
  display: block;
  transition: 0.3s;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #B769C0;
}

/* Position and style the close button (top right corner) */
.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
#main {
  transition: margin-left .5s;
  padding: 20px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
""")

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
        self.addCSS("""
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

/* Add a black background color to the top navigation */
.topnav {
  background-color: #424242;
  overflow: hidden;
}

.topnav i {
  float: left;
}


.topnav button {
  float: left;
  padding: 14px 16px;
}


/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #4CAF50;
  color: white;
}""")

    def processSelfList(self, l_values):
        for val in l_values:
            if isinstance(val, Element):
                self.append(val)
            else:
                self.append(Link(val))
