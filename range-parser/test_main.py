import unittest


# "2" -> [2]
# "5-10" -> [5, 6, 7, 8, 9, 10]
# "1-10,14, 20-25:2" -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]

def range_parser(ranges):
    numbers = ranges.split(',')

    result = []
    for n in numbers:
        if n.isdigit():
            add_number_to_list(n, result)
        else:
            add_range_to_list(n, result)

    return result


def add_range_to_list(input_range, result):
    start, end = input_range.split('-')

    numbers = range(int(start), int(end) + 1)
    for n in numbers:
        add_number_to_list(n, result)


def add_number_to_list(number, numbers):
    numbers.append(int(number))


class RangeParser(unittest.TestCase):
    def test_single_number(self):
        result = range_parser("2")

        expected = [2]
        self.assertEqual(expected, result)

    def test_multiple_numbers(self):
        result = range_parser("2,3,5")

        expected = [2, 3, 5]
        self.assertEqual(expected, result)

    def test_single_range(self):
        result = range_parser("2-5")

        expected = [2, 3, 4, 5]
        self.assertEqual(expected, result)

    def test_multiple_range(self):
        result = range_parser("2-5, 7-11")

        expected = [2, 3, 4, 5, 7, 8, 9, 10, 11]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
