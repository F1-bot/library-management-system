import unittest
from src.library import Library
from src.book import Book
from src.magazine import Magazine

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell", 1949, "1234567890")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")
        self.magazine = Magazine("National Geographic", "Various", 2023, 1)

    def test_add_item(self):
        self.library.add_item(self.book1)
        self.assertEqual(len(self.library._items), 1)

    def test_remove_item(self):
        self.library.add_item(self.book1)
        self.library.remove_item(self.book1)
        self.assertEqual(len(self.library._items), 0)

    def test_search(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine)

        results = self.library.search("orwell")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

        results = self.library.search("geographic")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "National Geographic")

    def test_search_by_year(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine)

        results = self.library.search_by_year(1949)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_str_representation(self):
        self.library.add_item(self.book1)
        expected = "Library with 1 items"
        self.assertEqual(str(self.library), expected)
