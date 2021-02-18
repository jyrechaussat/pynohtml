import os
from datetime import datetime
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
    SpanText,
    DescName,
    DescTerm,
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
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "libs/js/uikit.min.js"))
        self.imports.append(Script(src=script_path))
        #self.imports.append(Script(src="https://cdn.jsdelivr.net/npm/uikit@3.6.16/dist/js/uikit.min.js"))
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


class BreadCrumb(UIKIT_Container):
    def __init__(self, inputs, disable=[], **kwargs):
        super().__init__(inputs, tag="ul", klass="uk-breadcrumb", **kwargs)
        self.disable = disable

    def make(self):
        result = []
        for index, elmt in enumerate(self):
            if isinstance(elmt, Element):
                toadd = elmt
            elif type(elmt) == str:
                toadd = Link("#", elmt)
            else:
                toadd = SpanText(str(elmt))

            if index in self.disable:
                toadd = ListElement(toadd, klass="uk-disabled")
            else:
                toadd = ListElement(toadd)

            result.append(toadd)

        return result


class Button(UIKIT_Container):
    def __init__(self, text, color="default", size="", **kwargs):
        allowed_colors = ["default", "primary", "secondary", "danger", "text", "link"]
        if color not in allowed_colors:
            raise ValueError(f"UIKIT Button color can only be one of {allowed_colors}, default='default'")

        klass = f"uk-button uk-button-{color}"

        allowed_sizes = ["", "small", "large"]
        if size not in allowed_sizes:
            raise ValueError(f"UIKIT Button size can only be one of {allowed_sizes}, default='' ")
        if size:
            klass += f" uk-button-{size}"
        super().__init__(text, tag="button", klass=klass, **kwargs)


class Card(UIKIT_Container):
    def __init__(self, title="", inputs=[], **kwargs):
        super().__init__(elements=inputs, klass="uk-card uk-card-default uk-card-body", **kwargs)
        self.title = title

    def make(self):
        result = [Header(self.title, klass="uk-card-title")]
        result.extend([x for x in self])
        return result


class CountDown(UIKIT_Container):
    def __init__(self, expiration_time, **kwargs):
        if type(expiration_time) == str:
            datetime.fromisoformat(expiration_time)  # verification
            expi = expiration_time
        elif type(expiration_time) == datetime:
            expi = expiration_time.isoformat()
        else:
            raise ValueError("expiration_time should be isoformat ex: 2017-12-04T22:00:00+00:00 or type datetime")
        countdown = f"date: {expi}"
        super().__init__(klass="uk-grid-small uk-child-width-auto", uk_grid=True, uk_countdown=countdown, **kwargs)

    def make(self):
        result = []
        for digit in ["days", "hours", "minutes", "seconds"]:
            cell = UIKIT_Container(klass=f"uk-countdown-number uk-countdown-{digit}")
            legend = UIKIT_Container(digit.capitalize(),
                                     klass=f"uk-countdown-label uk-margin-small uk-text-center uk-visible@s")
            result.append(Container([cell, legend]))
            if digit != "seconds":
                result.append(UIKIT_Container(":", klass="uk-countdown-separator"))
        return result


class DescList(UIKIT_Container):
    def __init__(self, values, divider=False, **kwargs):
        if type(values) != dict \
           and any([(isinstance(v, DescName) or isinstance(v, DescTerm)) for v in values]):
            raise ValueError("DescList values argument should be of dict type where keys are DescName and values are DescTerm. \nOtherWise it should be a list of DescName/DescTerm objects")
        self.values = values
        klass = "uk-description-list"
        if divider:
            klass += " uk-description-list-divider"
        super().__init__(tag="dl", klass=klass, **kwargs)

    def make(self):
        result = []
        if type(self.values) == dict:
            for key, values in self.values.items():
                result.append(DescTerm(key))
                if type(values) == list:
                    for val in values:
                        result.append(DescName(val))
                else:
                    result.append(DescName(val))

        elif type(self.values) == list:
            result.extend(self.values)
        else:
            raise ValueError("Do not understand the type of DescList Input")

        return result


class Divider(UIKIT_Container):
    def __init__(self, vertical=False, icon=False, small=False, **kwargs):
        config = ""
        if icon:
            config = "-icon"
        if small:
            config = "-small"
        if vertical:
            config = "-vertical"
        klass = f"uk-divider{config}"
        super().__init__(tag="hr", klass=klass, **kwargs)


class Icon(UIKIT_Container):
    def __init__(self, icon, ratio="", **kwargs):
        if ratio and (type(ratio) == str and ratio.isdigit() or type(ratio) in [int, float]):
            icon = f"icon:{icon}; ratio:{ratio}"
        else:
            icon = f"{icon}"
        super().__init__(tag="span", uk_icon=icon, **kwargs)
        self.imports.append(Script("https://cdn.jsdelivr.net/npm/uikit@3.6.16/dist/js/uikit-icons.min.js"))


class IconLink(UIKIT_Container):
    def __init__(self, icon, link="#", ratio="", **kwargs):
        if ratio and (type(ratio) == str and ratio.isdigit() or type(ratio) in [int, float]):
            icon = f"icon:{icon}; ratio:{ratio}"
        else:
            icon = f"{icon}"
        link = kwargs.get("href", link)
        super().__init__(tag="a", uk_icon=icon, href=link, klass="uk-icon-button", **kwargs)
        self.imports.append(Script("https://cdn.jsdelivr.net/npm/uikit@3.6.16/dist/js/uikit-icons.min.js"))


class Label(UIKIT_Container):
    def __init__(self, text, color="", **kwargs):
        allowed_colors = ["", "success", "warning", "danger"]
        if color not in allowed_colors:
            raise ValueError(f"Label color cannot be othert than {allowed_colors}")

        if color:
            klass = f"uk-label-{color}"
        else:
            klass = "uk-label"
        super().__init__(text, tag="span", klass=klass)



class Section(UIKIT_Container):
    def __init__(self, elemenents=[], color="default", title="", title_size=3,  **kwargs):
        allowed_colors = ["default", "muted", "primary", "secondary"]
        if color not in allowed_colors:
            raise ValueError(f"UIKIT Button color can only be one of {allowed_colors}, default='default'")
        klass = f"uk-section uk-section-{color} uk-preserve-color"
        super().__init__(elemenents=elemenents, klass=klass)
        self.title = title
        self.title_size = title_size

    def make(self):
        result = []
        if self.title:
            result.append(Header(self.title, size=self.title_size))
        result.extend(self)

        return Container(result, klass="uk-container")


class Spinner(UIKIT_Container):
    def __init__(self, ratio="", **kwargs):
        uk_spinner = True
        if ratio and (type(ratio) == str and ratio.isdigit() or type(ratio) in [int, float]):
            uk_spinner = f"ratio:{ratio}"
        super().__init__(uk_spinner=uk_spinner, **kwargs)

