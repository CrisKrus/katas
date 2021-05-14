import unittest


def fill_char_frequency(current_char_index, characters, dictionary):
    if len(characters) is current_char_index:
        return dictionary

    character = characters[current_char_index]
    if character not in dictionary:
        frequency = characters.count(character)
        dictionary[character] = frequency

    return fill_char_frequency(current_char_index + 1, characters, dictionary)


def first_non_repeating_letter(letters):
    # selecciono primer caracter
    # cuento apariciones en la cadena
    # add to dictionary
    # selecciono siguiente caracter
    # busco en dicctionario si existe
    # si existe paso al siguiente
    # si no cuento
    # reviso el diccionario y me quedo con los caracteres que solo aparece una vez
    # busco que caracter aparece antes
    char_frequency = {}
    fill_char_frequency(0, letters, char_frequency)
    frequency_one_chars = get_frquency_one_characters(char_frequency)

    for character in frequency_one_chars:
        return character

    return ""


def get_frquency_one_characters(char_frequency):
    frequency_one_chars = []
    for character in char_frequency:
        if char_frequency[character] == 1:
            frequency_one_chars.append(character)
    return frequency_one_chars


# X "a" -> "a"
# X "aa" -> ""
#   "stress" -> "t", since the letter t only occurs once in the string, and occurs first in the string.
#   "moonmen" -> "e"


class Kata(unittest.TestCase):
    def test_one_letter_should_result_same_letter(self):
        first_char = first_non_repeating_letter("a")

        expected = "a"
        self.assertEqual(expected, first_char)

    def test_same_letter_repeated_multiple_times_should_result_on_empty_text(self):
        first_char = first_non_repeating_letter("aaaa")

        expected = ""
        self.assertEqual(expected, first_char)

    def test_multiple_letters_result_on_first_non_repeated_letter(self):
        first_char = first_non_repeating_letter("aaaao")

        expected = "o"
        self.assertEqual(expected, first_char)


if __name__ == '__main__':
    unittest.main()
