from elements import *
import unittest


class Test_Area(unittest.TestCase):
    def setUp(self):
        self.ins = Area()
        self.expected_html = "<area>"

    def test_expeected_html(self):
        self.assertEqual(self.ins.html, self.expected_html)


class Test_list(unittest.TestCase):
    def test_no_input(self):
        ins = List()
        expected_html = """<ul></ul>"""
        self.assertEqual(ins.html, expected_html)

    def test_append(self):
        ins = List()
        ins.append(Area())
        self.assertEqual(ins.html, """<ul>\n<li><area></li>\n</ul>""")
        ins.append(Area())
        self.assertEqual(ins.html, """<ul>\n<li><area></li>\n<li><area></li>\n</ul>""")

if __name__ == "__main__":
    unittest.main()
