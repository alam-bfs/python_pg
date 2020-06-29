class Person:

    def __init__(self, name):
        self.name = name
        self.maximum_books = 3

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_maximum_books(self, max_books):
        self.maximum_books = max_books

    def get_maximum_books(self):
        return self.maximum_books
