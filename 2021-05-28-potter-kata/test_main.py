import unittest


def potter_basket(book_list):
    sorted_book_list = sorted(book_list, reverse=True)

    if sorted_book_list[0] is 0:
        return 0

    most_buy_book = sorted_book_list[0]

    pack = sorted_book_list.count(most_buy_book)

    if pack is 2:
        rest = sorted_book_list[0] - sorted_book_list[2]
        bill = rest * 8 * 2
        bill -= bill * 0.05

        sorted_book_list[0] = sorted_book_list[1] = sorted_book_list[2]

        return bill + potter_basket(sorted_book_list)

    return sorted_book_list[0] * 8

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


if __name__ == '__main__':
    unittest.main()
