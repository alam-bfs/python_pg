import unittest


class Calc(unittest.TestCase):

    num1 = 0
    num2 = 0

    def test_add_two_numbers(self):
        assert 7 == self.num1 + self.num2

    def test_sub_two_numbers(self):
        assert 3 == self.num1 - self.num2

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())


if __name__ == "__main__":
    Calc.num1 = 5
    Calc.num2 = 2
    unittest.main()
