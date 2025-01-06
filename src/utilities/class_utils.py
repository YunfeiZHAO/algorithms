""" utilies for class test"""
from importlib import import_module
import unittest
import tomli

from iterable.list_tool import replace_recursive

class DynamicTestCase(unittest.TestCase):
    """ Placeholder for the test cases"""
    pass


class GenerateClassTestCase():
    """ Test classes with config"""
    def __init__(self, config_path):
        super().__init__()
        # parse from the configuration file
        try:
            self.config_path = config_path
            with open(self.config_path, "rb") as f:
                self.conf = tomli.load(f)
        except FileNotFoundError:
            print(f"File not found {self.config_path}")
        # get module
        try:
            self.module_name = self.conf['module']
            self._module = import_module(self.module_name)
        except ModuleNotFoundError:
            print(f"Module {self.module_name} not found.")
        except AttributeError as e:
            print(f"Error: {e}")
        self.instance = None
        print(f"Test module: {self.module_name}")
        print(f"Configuration path: {self.config_path}")
        self.set_test_func()

    def generate_case(
            self,
            instance,
            input_function,
            input_params,
            expected):
        """ Generate a test case"""
        def case(self):
            # cls = getattr(self._module, class_name)
            # instance = cls(*init_args)
            for func, params, gt in zip(
                input_function,
                input_params,
                expected
            ):
                # get method from the instance by name
                method = getattr(instance, func)
                # run the function
                output= method(*params)
                self.assertEqual(output, gt)
        return case

    def set_test_func(self):
        """ add test cases in unittest.TestCase"""
        for case in self.conf['cases']:
            expected = case['expected']
            # "None" in toml file is needed to be replaced
            replace_recursive(expected, "None", None)

            cls = getattr(self._module, case['class'])
            instance = cls(*case['init_args'])

            setattr(DynamicTestCase,
                    f"test_{case['name']}",
                    self.generate_case(
                        instance,
                        case['input_function'],
                        case['input_params'],
                        expected)
                    )

if __name__ == "__main__":
    GenerateClassTestCase("example.toml")
    unittest.main()
