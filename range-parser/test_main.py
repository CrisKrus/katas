import unittest


class MyTestCase(unittest.TestCase):
    def test_should_fail(self):
        self.assertEqual(True, False)

    def test_should_pass(self):
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
