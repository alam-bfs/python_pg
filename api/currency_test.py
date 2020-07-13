import unittest
from api import currency
from mock import Mock


class TestCurrency(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_post_comments(self):
        mock_post_comments = Mock()
        currency.post_comments(mock_post_comments, 'message')


if __name__ == '__main__':
    unittest.main()
