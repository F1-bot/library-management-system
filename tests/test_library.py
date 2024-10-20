import unittest
from src.library import Library
from src.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Test Book", "Test Author", 2023, "1234567890")

    def test_add_item(self):
        self.library.add_item(self.book)
        self.assertEqual(len(self.library._items), 1)

    def test_remove_item(self):
        self.library.add_item(self.book)
        self.library.remove_item(self.book)
        self.assertEqual(len(self.library._items), 0)

    def test_str_representation(self):
        self.library.add_item(self.book)
        expected = "Library with 1 items"
        self.assertEqual(str(self.library), expected)
