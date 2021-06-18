import unittest


def in_array(list1, list2):
    result = []

    for word1 in list1:
        for word2 in list2:
            if word1 not in result and word1 in word2:
                result.append(word1)

    return result


class Kata(unittest.TestCase):
    def test_one_word_is_in_second_list(self):
        a1 = ['arp']
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = ['arp']
        self.assertEqual(expected, result)

    def test_which_are_in(self):
        a1 = ['arp', 'live', 'strong']
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = ['arp', 'live', 'strong']
        self.assertEqual(expected, result)

    def test_result_should_be_ordered(self):
        a1 = ['live', 'arp', 'strong']
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = ['arp', 'live', 'strong']
        self.assertEqual(expected, result)

    def test_no_matches_found(self):
        a1 = ["tarp", "mice", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = []
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
