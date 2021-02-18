from pynohtml.fundamentals import (
    Container,
    Script,
    HeadLink,
)


class Semantic(Container):
    def __init__(self, elements=[], **kwargs):
        super().__init__(elements=elements, **kwargs)
