import unittest


def potter_basket(book_list):
    bill = 0

    for book in book_list:
        bill += book * 8

    return bill


class PotterKata(unittest.TestCase):
    def test_should_calculate_multiple_books_price(self):
        book_list = [0, 2, 0, 0, 0]
        # book_list2 = {
        #     'first': 0,
        #     'second': 1,
        #     'third': 0,
        #     'fourth': 0,
        #     'fifth': 0,
        # }

        total_bill = potter_basket(book_list)

        expected_price = 16
        self.assertEqual(expected_price, total_bill)


if __name__ == '__main__':
    unittest.main()
