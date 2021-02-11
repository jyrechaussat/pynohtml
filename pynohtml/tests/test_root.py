import unittest
from root import (
    SimpleElement,
    Container,
    ImportsLibrary,
    HeadLink,
    Base,
    Style,
    Script,
    Javascript,
)


class Test_SimpleElement(unittest.TestCase):
    def test_simple_element_simplest_input(self):
        tag = "simple"
        se = SimpleElement(tag)
        self.assertEqual(se.html, f"<{tag}>")

    def test_simple_element_with_class(self):
        tag = "simple"
        se = SimpleElement(tag, klass="aClass")
        self.assertEqual(se.html, f'<{tag} class="aClass">')

    def test_simple_element_with_attribute(self):
        tag = "simple"
        se = SimpleElement(tag, background_color="blue")
        self.assertEqual(se.html, f'<{tag} background_color="blue">')

    def test_simple_element_with_attribute_bool(self):
        tag = "simple"
        se = SimpleElement(tag, enabled=True)
        self.assertEqual(se.html, f'<{tag} enabled>')

    def test_simple_element_with_attributes_class_and_bool(self):
        tag = "simple"
        se = SimpleElement(tag, klass="aClass", enabled=True, background_color="blue")
        self.assertEqual(se.html, f'<{tag} enabled background_color="blue" class="aClass">')
        se = SimpleElement(tag, klass="aClass", enabled=False, background_color="blue")
        self.assertEqual(se.html, f'<{tag} background_color="blue" class="aClass">')


class Test_Container(unittest.TestCase):
    def test_container_simple_input(self):
        co = Container()
        self.assertEqual(co.html, "<div></div>")

    def test_container_with_one_elmt(self):
        co = Container()
        co.append(SimpleElement("simple"))
        self.assertEqual(co.html, "<div>\n<simple>\n</div>")

    def test_container_with_two_elmt_using_append(self):
        co = Container()
        so = SimpleElement("simple")
        co.append(so)
        co.append(so)
        self.assertEqual(co.html, "<div>\n<simple>\n<simple>\n</div>")

    def test_container_with_two_elmt_using_extend(self):
        co = Container()
        so = SimpleElement("simple")
        co.extend([so, so])
        self.assertEqual(co.html, "<div>\n<simple>\n<simple>\n</div>")

    def test_container_with_attributes(self):
        co = Container(klass="aClass", enabled=True, background_color="blue")
        so = SimpleElement("simple")
        co.extend([so, so])
        self.assertEqual(co.html, """<div enabled background_color="blue" class="aClass">
<simple>
<simple>
</div>""")


class Test_HeadLink(unittest.TestCase):
    def setUp(self):
        self.data = "main.css"
        self.imp = HeadLink(self.data)
        self.other_imp = HeadLink("other.css")
        self.expected_html = '<link rel="stylesheet" href="main.css">'

    def test_data_is_set(self):
        self.assertEqual(self.imp.data, self.data)

    def test_html_is_equal_to_expected_html(self):
        self.assertEqual(self.imp.html, self.expected_html)

    def test_two_same_import_instance_different_data_is_different(self):
        self.assertFalse(self.imp == self.other_imp)

    def test_hash(self):
        se = set()
        se.add(self.imp)
        self.assertEqual(len(se), 1)
        se.add(self.imp)
        self.assertEqual(len(se), 1)
        se.add(self.other_imp)
        self.assertEqual(len(se), 2)


class Test_Base(Test_HeadLink):
    def setUp(self):
        self.data = "http://www.example.com/"
        self.imp = Base(self.data)
        self.other_imp = HeadLink("http://www.example2.com/")
        self.expected_html = '<base href="http://www.example.com/" target="_blank">'


class Test_Style(Test_HeadLink):
    def setUp(self):
        self.data = """h1 {color:red;}\np {color:blue;}"""
        self.imp = Style(self.data)
        self.other_imp = Style(self.data + "2")
        self.expected_html = f"<style>\n{self.data}\n</style>"


class Test_Script(Test_HeadLink):
    def setUp(self):
        self.data = ""
        self.imp = Script("myscript.js")
        self.other_imp = Style("myotherscript.js")
        self.expected_html = '<script src="myscript.js"></script>'


class Test_Javascript(Test_HeadLink):
    def setUp(self):
        self.data = 'document.getElementById("demo").innerHTML = "Hello JavaScript!";"'
        self.imp = Javascript(self.data)
        self.other_imp = Javascript(self.data * 2)
        self.expected_html = '<script type="text/javascript">\ndocument.getElementById("demo").innerHTML = "Hello JavaScript!";"\n</script>'


class Test_ImportsLibrary(unittest.TestCase):
    def test_whole_singleton(self):
        il = ImportsLibrary()
        self.assertIsNotNone(il.instance)
        self.assertEqual(len(il), 0)

        # test_add_one_import_instance
        imp = Script("file.js")
        il.append(imp)
        self.assertEqual(len(il), 1)

        # test_add_more_than_one_instnace
        imp2 = HeadLink("main.css")
        imp3 = Base("http://hello.com")
        il.extend([imp2, imp3])
        self.assertEqual(len(il), 3)

        # test_add_twice_the_same_instance
        imp4 = HeadLink("main.css")
        il.append(imp4)
        self.assertEqual(len(il), 3)

        # test_singleton_one_instance
        other_il = ImportsLibrary()
        self.assertEqual(len(other_il), 3)

if __name__ == "__main__":
    unittest.main()
