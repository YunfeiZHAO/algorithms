""" unit test entry point"""
import sys
import unittest
import argparse
from utilities.class_utils import GenerateClassTestCase, DynamicTestCase
# DynamicTestCase is needed to be imported as the test cases is added to it.

def main(args):
    """ Entry point """
    GenerateClassTestCase(args.config_path)

    # Remove --config_path from sys.argv to avoid conflict with unittest
    sys.argv = sys.argv[:1]
    unittest.main()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run unit tests with a specified configuration file.")
    parser.add_argument('--config_path', type=str, required=True,
                        help='Path to the configuration file')
    args = parser.parse_args()
    main(args)
