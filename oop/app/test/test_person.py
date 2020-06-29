import unittest

from oop.app.src.person import Person


class PersonTestCase(unittest.TestCase):

    def setUp(self):
        self.person = Person('Kaiser')

    def tearDown(self):
        self.person = None

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'Kaiser', 'incorrect default name')

    def test_get_maximum_books(self):
        self.assertEqual(self.person.get_maximum_books(), 3, 'incorrect default maximum books')


if __name__ == '__main__':
    unittest.main()
