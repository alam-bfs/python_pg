

class Book:

    person = None

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_person(self, person):
        self.person = person

    def get_person(self):
        return self.person


class MyLibrary:

    name = None

    def __init__(self, name):
        self.name = name
        self.books = []
        self.people = []

    def add_book(self, book):
        self.books.append(book)

    def add_person(self, person):
        self.people.append(person)

    def remove_book(self, book):
        self.books.remove(book)

    def remove_person(self, person):
        self.people.remove(person)

    def get_books(self):
        return self.books

    def get_people(self):
        return self.people

    def get_available_books(self):
        return self.books

    def get_checked_out_books(self):
        pass

    def get_books_for_person(self):
        pass

    @staticmethod
    def check_out_book(book, person):
        if book.get_person() is None:
            book.set_person(person)
            return True
        else:
            return False

    @staticmethod
    def check_in_book(book):
        if book.get_person is not None:
            book.set_person(None)
            return True
        else:
            return False

    def get_books_for_person(self, person):
        result = []

        for aBook in self.get_books():
            if aBook.get_person() is not None and aBook.get_person().get_name() == person.get_name():
                result.append(aBook)
        return result


if __name__ == '__main__':
    john = Person('John')
    # book = Book('Harry Potters', 'Smith')
    # book.set_person(john)
    #
    # print(john.get_maximum_books())

