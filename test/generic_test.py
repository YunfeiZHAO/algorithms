""" Generic test class"""
import json
import unittest

from iterable.string_tool import divide_simply


class GenericTestCase(unittest.TestCase):
    """ Generic test class """
    def __init__(
        self,
        methodName='runTest',
        function_to_test=None,
        test_data_file=None):

        super(GenericTestCase, self).__init__(methodName)
        self.function_to_test = function_to_test
        self.test_data_file = test_data_file
        self.test_cases = None

    def setUp(self):
        """ Load test case method from json file, all test casses in a module is saved in a json file"""
        with open(self.test_data_file, 'r', encoding='utf-8') as file:
            module_test = json.load(file)
            self.test_cases = module_test[self.function_to_test.__name__]

    def test_function(self):
        """ sub tests function """
        for case in self.test_cases:
            input_data = case["input"]
            expected = case["expected"]
            with self.subTest(input_data=input_data, expected=expected):
                result = self.function_to_test(*input_data)
                self.assertEqual(result, expected)

# Setup the test suite
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(
        GenericTestCase(
            function_to_test=divide_simply,
            test_data_file=r'C:\Users\yzhao04\workspace\algorithms\test\iterable\string_test.json'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
