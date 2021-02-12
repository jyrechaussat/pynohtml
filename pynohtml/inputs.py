from fundamentals import (
    Element,
    Container
)


class Input(Element):
    def __init__(self, label_before="", label_after="", sep="", **kwargs):
        super().__init__(**kwargs)
        self.sep = sep
        self.label_after = label_after
        self.label_before = label_before

    @property
    def html(self):
        css = self.processCss()
        return f"{self.label_before}{self.sep}<input{css}>{self.label_after}"


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
    def __init__(self, name, value, checked=False, **kwargs):
        super().__init__(name=name, value=value, type="radio", checked=checked, **kwargs)


class CheckBox(Input):
    def __init__(self, name, value, checked=False, **kwargs):
        super().__init__(name=name, value=value, type="checkbox", checked=checked, **kwargs)


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

    @property
    def html(self):
        css = self.processCss()
        return f"<textarea{css}>{self.sep}" + str(self.value) + f"{self.sep}</textarea>"


class Option(Container):
    def __init__(self, label="", **kwargs):
        super().__init__(label, tag="option", sep="", **kwargs)


class OptGroup(Container):
    def __init__(self, label, options, **kwargs):
        super().__init__(options, tag="optgroup", label=label, **kwargs)

    def make(self):
        return [opt if isinstance(opt, Option) else Option(opt) for opt in self]


class SelectInput(Container):
    def __init__(self, options, **kwargs):
        self.options = options
        super().__init__(tag="select", **kwargs)

    def make(self):
        result = []
        if type(self.options) == dict:
            for label, values in self.options.items():
                result.append(OptGroup(label, values))
        elif type(self.options) == list:
            for opt in self.options:
                result.append(opt if type(opt) in [Option, OptGroup] else Option(opt))


class DataList(Container):
    def __init__(self, values=[], **kwargs):
        super().__init__(values, tag="datalist", sep="", **kwargs)

    def make(self):
        result = []
        for val in self:
            if isinstance(val, Option):
                result.append(val)
            elif type(val) == str:
                result.append(Option(value=val))
            else:
                raise ValueError("DataList cannot take any other arguments than pynohtml.Option or string defining option value attribute")
        return result
