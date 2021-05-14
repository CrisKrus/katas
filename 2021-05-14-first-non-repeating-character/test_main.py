import unittest


def first_non_repeating_letter(letters):
    return letters

# X "a" -> "a"
#   "aa" -> ""
#   "stress" -> "t", since the letter t only occurs once in the string, and occurs first in the string.
#   "moonmen" -> "e"


class Kata(unittest.TestCase):
    def test_one_letter_should_result_same_letter(self):
        first_char = first_non_repeating_letter("a")

        self.assertEqual("a", first_char)

    def test_same_letter_repeated_multiple_times_should_result_on_empty_text(self):
        first_char = first_non_repeating_letter("aaaa")

        self.assertEqual("", first_char)



if __name__ == '__main__':
    unittest.main()
