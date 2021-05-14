import unittest


def first_non_repeating_letter(letters):
    return letters

# "a" -> "a"
# "aa" -> ""
# "stress" -> "t", since the letter t only occurs once in the string, and occurs first in the string.
# "moonmen" -> "e"


class Kata(unittest.TestCase):
    def test_one_letter_should_return_same_letter(self):
        first_char = first_non_repeating_letter("a")

        self.assertEqual("a", first_char)


if __name__ == '__main__':
    unittest.main()
