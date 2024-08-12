from Books.Book import Book


class Contacts(Book):
    def __str__(self):
        return "Name, Address, Phone, Email, Birthday\n" + super().__str__()