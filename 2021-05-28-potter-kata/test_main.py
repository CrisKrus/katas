import unittest


def fill_list_with_value_until_index(list_to_fill, value, last_index):
    res = []

    for i in range(len(list_to_fill)):
        current_value = list_to_fill[i]
        res.append(value) if i <= last_index else res.append(current_value)

    return res


def potter_basket(book_list):
    sorted_book_list = sorted(book_list, reverse=True)

    if sorted_book_list[0] is 0:
        return 0

    most_buy_book = sorted_book_list[0]

    pack = sorted_book_list.count(most_buy_book)

    if pack is 2:
        second_most_buy_book = sorted_book_list[2]

        bill = calculate_discount(pack, most_buy_book, second_most_buy_book)

        sorted_book_list = fill_list_with_value_until_index(sorted_book_list, second_most_buy_book, 1)

        return bill + potter_basket(sorted_book_list)

    elif pack is 3:
        second_most_buy_book = sorted_book_list[3]

        bill = calculate_discount(pack, most_buy_book, second_most_buy_book)

        sorted_book_list = fill_list_with_value_until_index(sorted_book_list, second_most_buy_book, 2)

        return bill + potter_basket(sorted_book_list)

    elif pack is 4:
        second_most_buy_book = sorted_book_list[4]

        bill = calculate_discount(pack, most_buy_book, second_most_buy_book)

        sorted_book_list = fill_list_with_value_until_index(sorted_book_list, second_most_buy_book, 3)

        return bill + potter_basket(sorted_book_list)

    elif pack is 5:
        second_most_buy_book = 0

        bill = calculate_discount(pack, most_buy_book, second_most_buy_book)

        sorted_book_list = fill_list_with_value_until_index(sorted_book_list, second_most_buy_book, 4)

        return bill + potter_basket(sorted_book_list)

    return sorted_book_list[0] * 8


def calculate_discount(pack, most_buy_book, second_most_buy_book):
    rest = most_buy_book - second_most_buy_book
    bill = rest * 8 * pack

    if pack is 2:
        return bill * 0.95

    if pack is 3:
        return bill * 0.90

    if pack is 4:
        return bill * 0.80

    if pack is 5:
        return bill * 0.75

    return bill


# 2 books 5% discount
# 3 books 10% discount
# 4 books 20% discount
# 5 books 25% discount

# 1 0 0 0 0 1*8
# 1 1 0 0 0 2*8-5
# 2 1 1 0 0 1*8 + 3*8-10


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


if __name__ == '__main__':
    unittest.main()
