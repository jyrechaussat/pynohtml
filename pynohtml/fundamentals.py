

def debugprint(data):
	print("#" * 40)
	print(data)
	print("#" * 40)

# TODO : add class variable theme and change it in htmlMaker

class Element(object):
	def __init__(self, klass="", imports=[], **kwargs):
		self.base_html = ""
		self.css_dict = kwargs
		self.css = ""
		if type(imports) != list:
			self.imports = [imports]
		else:
			self.imports = imports
		self.klass = klass

	def processCss(self):
		if self.klass:
			self.css = 'class="{KLASS}"'.format(KLASS=self.klass)
		
		self.css += " "
		for key, value in self.css_dict.items():
			if type(value) == bool:
				self.css += key
			else:
				self.css += '{K}="{V}"'.format(K=key, V=value)

			self.css += " "

	def addScript(self, imp ):
		self.imports.append(Script(imp))

	def addHLink(self, link):
		self.imports.append(HeadLink(link))

	def addJs(self, js):
		self.imports.append(Javascript(js))

	def addCSS(self, css):
		self.imports.append(CSSStyle(css))

	def addStyle(self, style):
		self.imports.append(Style(style))

	def getImports(self):
		return self.imports

	def postProcess(self):
		pass

	def __str__(self):
		self.postProcess()
		self.processCss()
		return self.base_html.format(X = self)

class SimplestElement(Element):
	def __init__(self, tag, **kwargs):
		super().__init__(**kwargs)
		self.tag = tag
		self.base_html = "<{X.tag} {X.css}>"

class Container(list, Element):
	def __init__(self, elements=[], tag = "div", sep = "\n", **kwargs):
		list.__init__(self, [])
		Element.__init__(self, **kwargs)
		if type(elements) not in [list, dict]:
			elements = [elements]
		self.processSelfList(elements)
		self.tag = tag
		self.sep = sep

	def getImports(self):
		result = []
		for element in list(self):
			if isinstance(element, Element):
				result.extend(element.getImports())
		result.extend(self.imports)
		return result

	def processSelfList(self, l_values):
		self.extend(l_values)

	def postProcess(self):
		return self.sep.join([str(element) for element in list(self)])
	
	def __str__(self):
		self.processCss()
		self.base_html = "<{X.tag} {X.css}>{X.sep}"
		self.base_html += self.postProcess()
		self.base_html += "{X.sep}</{X.tag}>"
		return self.base_html.format(X = self)

class Theme(object):
	def __init__(self, links=[], scripts = [], attr_mapping={}):
		self.links = links
		self.scripts = scripts
		self.attr_mapping = {}


class Import(Element):
	inHead = True
	isLink = False
	def __init__(self, data, tag="script", sep="\n", **kwargs):
		super().__init__(**kwargs)
		self.data = data
		self.tag = tag
		self.sep = sep
		if self.isLink:
			self.base_html = "<{X.tag} {X.css}>{X.sep}</{X.tag}>"
		else:
			self.base_html = "<{X.tag} {X.css}>{{DATA}}</{X.tag}>{X.sep}"

	def __hash__(self):
		return hash(self.data)

	def __eq__(self, other):
		if isinstance(other, Import):
			return self.data == other.data
		elif type(other) == str:
			return self.data == other
		return False

class HeadLink(Import):
	isLink = True
	def __init__(self, link, rel="stylesheet", **kwargs):
		super().__init__(link, tag="link", rel=rel, href=link, **kwargs)

class Script(Import):
	isLink = True
	def __init__(self, src):
		super().__init__("", tag="script", sep="", src=src)

class BodyScript(Import):
	inHead = False
	def __init__(self, script):
		super().__init__(script, tag="script")

class Javascript(Import):
	inHead = False
	def __init__(self, script):
		super().__init__(script, tag="script", type="text/javascript")

class Style(Import):
	def __init__(self, style):
		super().__init__(style, tag="style")

class CSSStyle(Import):
	def __init__(self, style):
		super().__init__(style, tag="style", type="text/css")

class Base(Import):
	def __init__(self, src, target="_blank", **kwargs):
		super().__init__("", tag="base", href=src, target=target, **kwargs)
