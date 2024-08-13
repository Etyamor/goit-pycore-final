from Books.Book import Book
from typing import List
from Records.Contact import Contact


class Contacts(Book):
    def __str__(self):
        return "Name, Address, Phone, Email, Birthday\n" + super().__str__()
    
    def find_entity(self, text: str) -> List[Contact]:
        return [record for record in self.data if text in record.name.value or text == record.email.value]
