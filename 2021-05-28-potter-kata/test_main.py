import unittest


def potter_basket(book_amount):
    return 8


class PotterKata(unittest.TestCase):
    def test_should_calculate_one_book_price(self):
        book_list = [0, 1, 0, 0, 0]
        # book_list2 = {
        #     'first': 0,
        #     'second': 1,
        #     'third': 0,
        #     'fourth': 0,
        #     'fifth': 0,
        # }

        total_bill = potter_basket(book_list)

        expected_price = 8
        self.assertEqual(expected_price, total_bill)


if __name__ == '__main__':
    unittest.main()
