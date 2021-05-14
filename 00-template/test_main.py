import unittest


def main_func():
    return True


class Kata(unittest.TestCase):
    def test_should_work(self):
        true = main_func()
        self.assertTrue(true)

    def test_should_fail(self):
        true = main_func()
        self.assertFalse(true)


if __name__ == '__main__':
    unittest.main()
