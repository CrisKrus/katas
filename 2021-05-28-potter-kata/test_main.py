import unittest


def potter_basket(book_list):
    sorted_book_list = sorted(book_list, reverse=True)

    if sorted_book_list[0] is 0:
        return 0

    most_buy_book = sorted_book_list[0]
    pack_size = sorted_book_list.count(most_buy_book)
    second_most_buy_book = find_second_most_buy_book(pack_size, sorted_book_list)

    pack_amount = most_buy_book - second_most_buy_book

    pack_bill = calculate_discount(pack_size, pack_amount)

    sorted_book_list = fill_list_with_value_until_index(sorted_book_list, second_most_buy_book, pack_size)

    return pack_bill + potter_basket(sorted_book_list)


def find_second_most_buy_book(pack_size, sorted_book_list):
    if pack_size is 2:
        return sorted_book_list[2]
    elif pack_size is 3:
        return sorted_book_list[3]
    elif pack_size is 4:
        return sorted_book_list[4]
    return 0


def fill_list_with_value_until_index(list_to_fill, value, last_index):
    res = []

    for i in range(len(list_to_fill)):
        current_value = list_to_fill[i]
        res.append(value) if i <= last_index else res.append(current_value)

    return res


def calculate_discount(pack_size, pack_amount):
    bill = pack_amount * 8 * pack_size

    if pack_size is 2:
        return bill * 0.95

    if pack_size is 3:
        return bill * 0.90

    if pack_size is 4:
        return bill * 0.80

    if pack_size is 5:
        return bill * 0.75

    return bill


class PotterKata(unittest.TestCase):
    def test_should_calculate_multiple_books_price(self):
        book_list = [0, 2, 0, 0, 0]

        total_bill = potter_basket(book_list)

        expected_price = 16
        self.assertEqual(expected_price, total_bill)

    def test_should_calculate_5_percent_discount(self):
        book_list = [1, 1, 0, 0, 0]

        total_bill = potter_basket(book_list)

        expected_price = 15.2
        self.assertEqual(expected_price, total_bill)

    def test_should_calculate_10_percent_discount(self):
        book_list = [1, 1, 0, 1, 0]

        total_bill = potter_basket(book_list)

        expected_price = 21.6
        self.assertEqual(expected_price, total_bill)

    def test_should_calculate_20_percent_discount(self):
        book_list = [1, 1, 0, 1, 1]

        total_bill = potter_basket(book_list)

        expected_price = 25.6
        self.assertEqual(expected_price, total_bill)

    def test_should_calculate_25_percent_discount(self):
        book_list = [1, 1, 1, 1, 1]

        total_bill = potter_basket(book_list)

        expected_price = 30
        self.assertEqual(expected_price, total_bill)

    def test_should_calculate_multiple_discount(self):
        book_list = [2, 1, 2, 1, 2]

        total_bill = potter_basket(book_list)

        expected_price = 51.60
        self.assertEqual(expected_price, total_bill)


if __name__ == '__main__':
    unittest.main()
