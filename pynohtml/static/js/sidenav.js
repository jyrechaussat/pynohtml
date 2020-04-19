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

