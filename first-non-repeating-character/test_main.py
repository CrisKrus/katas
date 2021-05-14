import unittest


def first_non_repeating_letter(letters):
    return True


class Kata(unittest.TestCase):
    def test_should_work(self):
        true = first_non_repeating_letter("")
        self.assertTrue(true)

    def test_should_fail(self):
        true = first_non_repeating_letter("")
        self.assertFalse(true)


if __name__ == '__main__':
    unittest.main()
