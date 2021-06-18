import unittest


def in_array(list1, list2):
    return True


class Kata(unittest.TestCase):
    def test_one_word_is_in_second_list(self):
        a1 = ['arp']
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = ['arp']
        self.assertEqual(expected, result)

    def test_which_are_in(self):
        self.skipTest('final check')
        a1 = ['arp', 'live', 'strong']
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

        result = in_array(a1, a2)

        expected = ['arp', 'live', 'strong']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
