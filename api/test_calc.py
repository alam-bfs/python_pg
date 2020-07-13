import unittest
from api import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(5, 2)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
