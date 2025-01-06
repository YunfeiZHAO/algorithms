import unittest

class TestsContainer(unittest.TestCase):
    longMessage = True

def make_test_function(description, a, b):
    def test(self):
        self.assertEqual(a, b, description)
    return test

if __name__ == '__main__':
    testsmap = {
        'foo': [1, 1],
        'bar': [1, 2],
        'baz': [5, 5]}

    for name, params in testsmap.items():
        test_func = make_test_function(name, params[0], params[1])
        setattr(TestsContainer, 'test_{0}'.format(name), test_func)

    unittest.main()