import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node =  HTMLNode(tag="a", value="Google", props=props)

        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_empty_props(self):
        node = HTMLNode(tag="p", value="Hello world!")

        expected_output = ''
        self.assertEqual(node.props_to_html(), expected_output)

    def test_img_props(self):
        props = {"src": "image.jpg", "alt": "A description of the image"}
        node = HTMLNode(tag="img", value="image", props=props)

        expected_output = ' src="image.jpg" alt="A description of the image"'
        self.assertEqual(node.props_to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()