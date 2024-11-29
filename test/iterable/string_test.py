import unittest
from iterable.string_tool import divide_simply

class TestDivideSimply(unittest.TestCase):
    def test_no_common_chars(self):
        self.assertEqual(divide_simply('abc', 'def'), ('abc', 'def'))

    def test_some_common_chars(self):
        self.assertEqual(divide_simply('abbd', 'be'), ('abd', 'e'))

    def test_all_common_chars(self):
        self.assertEqual(divide_simply('abc', 'abc'), ('', ''))

    def test_empty_strings(self):
        self.assertEqual(divide_simply('', ''), ('', ''))

    def test_repeated_chars(self):
        self.assertEqual(divide_simply('aabbcc', 'abc'), ('abc', ''))

if __name__ == '__main__':
    unittest.main()