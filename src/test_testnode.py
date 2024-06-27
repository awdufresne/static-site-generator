import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    #test case, url property is None
    def test_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        print(f"$$$ node is : {node}")
        print(f"$$$ node is : {node2}")
        self.assertNotEqual(node, node2)
    
    #test case, text_types are different
    def test_text_type(self):    
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()