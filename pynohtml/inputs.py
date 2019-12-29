from kitchen.cockery import(
Element,
Container
)

class Input(Element):
	def __init__(self, label_before="", label_after="", sep="", **kwargs):
		super().__init__(**kwargs)
		self.sep = sep
		self.label_after = label_after
		self.label_before = label_before
		self.base_html = "{X.label_before}{X.sep}<input {X.css}>{X.label_after}"

class InputButton(Input):
	def __init__(self, value, onclick, **kwargs):
		super().__init__(value=value, type="button", **kwargs)

class Submit(Input):
	def __init__(self, value, **kwargs):
		super().__init__(value=value, type="submit")

class TextInput(Input):
	def __init__(self, name, value, **kwargs):
		super().__init__(name=name, value=value, type="text", **kwargs)

class ResetInput(Input):
	def __init__(self, name, value, **kwargs):
		super().__init__(name=name, value=value, type="reset", **kwargs)

class RadioInput(Input):
	def __init__(self, name, value, checked = False, **kwargs):
		super().__init__(name=name, value=valye, type="radio", checked=checked)

class CheckBox(Input):
	def __init__(self, name, value, checked = False, **kwargs):
		super().__init__(name=name, value=value, type="checkbox", checked=checked)

class DateInput(Input):
	def __init(self, name, min="", max="", **kwargs):
		super().__init__(name, "", typ="date")

class FileInput(Input):
	def __init__(self, name, **kwargs):
		super().__init__(name=name, type="file", **kwargs)

class TextArea(Element):
	def __init__(self, name, value="", **kwargs):
		super().__init__(name=name, **kwargs)
		self.base_html = "<textarea {X.css}>\n{X.value}\n</textarea>"
		self.value = value

class Option(Container):
	def __init__(self, label, **kwargs):
		super().__init__(label, tag="option", sep="", **kwargs)

class OptGroup(Container):
	def __init__(self, label, options, **kwargs):
		super().__init__(options, tag="optgroup", label=label, **kwargs)

	def processSelfList(self, options):
		for opt in options:
			if isinstance(opt, Option):
				self.append(opt)
			else:
				self.append(Option(opt))

class SelectInput(Container):
	def __init__(self, options, **kwargs):
		super().__init__(options, tag="select", **kwargs)

	def processSelfList(self, options):
		if type(options) == dict:
			for label, values in options.items():
				self.append(OptGroup(label, values))
		elif type(options) == list:
			for opt in options:
				self.append(opt if type(opt) in [Option, OptGroup] else Option(opt))

class Option(SimplestElement):
    def __init__(self, **kwargs):
        super().__init__("option", **kwargs)

class DataList(Container):
    def __init__(self, values=[], **kwargs):
        super().__init__(values, tag="datalist", sep="", **kwargs)

    def processSelfList(self, values):
        for val in values:
            if isinstance(val, Option):
                self.append(val)
            elif type(val) == str:
                self.append(Option(value=val))
            else:
                raise ValueError("DataList cannot take any other arguments than pynohtml.Option or string defining option value attribute")

