import unittest

class TestClassA(unittest.TestCase):
    def testOne(self):
        pass


class TestClassB(unittest.TestCase):
    def testOne(self):
        pass 


if __name__ == '__main__':
    test_classes_to_run = [TestClassA, TestClassB]
    loader = unittest.TestLoader()
    suites_list = []

    for testclass in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    overall_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)