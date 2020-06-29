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
