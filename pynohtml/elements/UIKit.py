from pynohtml.fundamentals import (
    Element,
    Container,
    Script,
    HeadLink,
)

from pynohtml import (
    Header,
    ListElement,
    Link,
)

class UIKIT_Container(Container):
    def __init__(self, elements=[], **kwargs):
        new_args = {}
        for key, value in kwargs.items():
            if key.startswith("uk") and "_" in key:
                new_args[key.replace("_", "-")] = value
            else:
                new_args[key] = value

        super().__init__(elements=elements, **new_args)
        self.imports.append(Script(src="https://cdn.jsdelivr.net/npm/uikit@3.6.16/dist/js/uikit.min.js"))
        self.imports.append(HeadLink("https://cdn.jsdelivr.net/npm/uikit@3.6.16/dist/css/uikit.min.css"))


class HContainer(UIKIT_Container):
    def __init__(self, inputs=[], divider=True, **kwargs):
        super().__init__(elements=inputs)
        self.divider = divider

    def make(self):
        klass = f"uk-column-1-{len(self)}"

        if self.divider:
            klass += " uk-column-divider"
        if self.css_dict.get("class", False):
            self.css_dict["class"] += " " + klass
        else:
            self.css_dict["class"] = klass
        return self


class UIKIT_Link(UIKIT_Container):
    def __init__(self, **kwargs):
        super().__init__(tag="a", **kwargs)

class Card(UIKIT_Container):
    def __init__(self, title="", inputs=[], **kwargs):
        super().__init__(elements=inputs, klass="uk-card uk-card-default uk-card-body", **kwargs)
        self.title = title

    def make(self):
        result = [Header(self.title, klass="uk-card-title")]
        result.extend([x for x in self])
        return result


class Alert(UIKIT_Container):
    def __init__(self, inputs=[], level="primary", add_close_button=True, **kwargs):
        if level not in ["primary", "success", "warning", "danger"]:
            raise ValueError("Alert level can only be 'primary', 'success', 'warning' or 'danger'")
        klass = f"uk-alert-{level}"
        self.add_close_button = add_close_button
        super().__init__(elements=inputs, klass=klass, uk_alert=True, **kwargs)

    def make(self):
        result = []
        if self.add_close_button:
            result.append(UIKIT_Link(klass="uk-alert-close", uk_close=True))
        result.extend([x for x in self])
        return result

class Accordion(UIKIT_Container):
    def __init__(self, accordions={}, collapsible=True, multiple=False, **kwargs):
        self.accordions = accordions
        if multiple:
            collapse_or_multiple = "multiple: true"
        elif not collapsible:
            collapse_or_multiple = "collapsible: false"
        else:
            collapse_or_multiple = collapsible


        super().__init__(klass="", tag="ul", uk_accordion=collapse_or_multiple, **kwargs)

    def make(self):
        result = []
        for title, content in self.accordions.items():
            title = Link("#", title, klass="uk-accordion-title")
            content_container = Container(content, klass="uk-accordion-content")
            result.append(ListElement([title, content_container]))

        return result

class Badge(UIKIT_Container):
    def __init__(self, value):
        super().__init__(value, tag="span", klass="uk-badge")
