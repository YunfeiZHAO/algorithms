""" unit test for list tool"""
import unittest

from iterable.list_tool import replace_recursive


class TestList(unittest.TestCase):
    def test_replace_recursive(self):
        l = [1,2, ["None", None, [1,2, "None"]], 'a']
        target = [1,2, [None, None, [1,2, None]], 'a']
        replace_recursive(l, "None", None)
        self.assertEqual(l, target)


if __name__ == "__main__":
    unittest.main()