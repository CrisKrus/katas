import unittest


def first_non_repeating_letter(characters):
    char_frequency = get_char_frequency(characters.lower())
    frequency_one_chars = get_frequency_one_characters(char_frequency)
    index_first_frequency_one_char = get_index_from_first_frequency_one_char(characters.lower(), frequency_one_chars)

    return "" if index_first_frequency_one_char == -1 else characters[index_first_frequency_one_char]


def fill_char_frequency(current_char_index, characters, char_frequency):
    if len(characters) is current_char_index:
        return char_frequency

    character = characters[current_char_index]
    if character not in char_frequency:
        frequency = characters.count(character)
        char_frequency[character] = frequency

    return fill_char_frequency(current_char_index + 1, characters, char_frequency)


def get_index_from_first_frequency_one_char(characters, frequency_one_chars):
    for c in characters:
        if c in frequency_one_chars:
            return characters.index(c)
    return -1


def get_char_frequency(letters):
    char_frequency = {}
    fill_char_frequency(0, letters, char_frequency)
    return char_frequency


def get_frequency_one_characters(char_frequency):
    frequency_one_chars = []
    for character in char_frequency:
        if char_frequency[character] == 1:
            frequency_one_chars.append(character)
    return frequency_one_chars


class FirstNonRepeatingCharacter(unittest.TestCase):
    def test_one_letter_should_result_same_letter(self):
        first_char = first_non_repeating_letter("a")

        expected = "a"
        self.assertEqual(expected, first_char)

    def test_same_letter_repeated_multiple_times_should_result_on_empty_text(self):
        first_char = first_non_repeating_letter("aaaa")

        expected = ""
        self.assertEqual(expected, first_char)

    def test_multiple_letters_result_on_first_non_repeated_letter(self):
        first_char = first_non_repeating_letter("stress")

        expected = "t"
        self.assertEqual(expected, first_char)

    def test_multiple_letters_in_multiple_cases_result_on_first_non_repeated_letter(self):
        first_char = first_non_repeating_letter("sTreSS")

        expected = "T"
        self.assertEqual(expected, first_char)


if __name__ == '__main__':
    unittest.main()
