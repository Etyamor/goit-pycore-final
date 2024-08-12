from Books.Book import Book


class Notes(Book):
    def __str__(self):
        return "Title, Note, Tags\n" + super().__str__()