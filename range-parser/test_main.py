import unittest


# "2" -> [2]
# "5-10" -> [5, 6, 7, 8, 9, 10]
# "1-10,14, 20-25:2" -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]

def range_parser(ranges):
    return [2]


class MyTestCase(unittest.TestCase):
    def test_single_number(self):
        result = range_parser("2")

        expected = [2]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
