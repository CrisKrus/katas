import unittest


# "2" -> [2]
# "5-10" -> [5, 6, 7, 8, 9, 10]
# "1-10,14, 20-25:2" -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]

def range_parser(ranges):
    result = ranges.split(',')

    foo = []
    for n in result:
        foo.append(int(n))

    return foo


class RangeParser(unittest.TestCase):
    def test_single_number(self):
        result = range_parser("2")

        expected = [2]
        self.assertEqual(expected, result)

    def test_multiple_numbers(self):
        result = range_parser("2,3,5")

        expected = [2, 3, 5]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
