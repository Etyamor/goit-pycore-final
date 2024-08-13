from typing import List, Union, Any
from Books.Book import Book
from Records.Contact import Contact

class Contacts(Book):
    def __str__(self):
        return "Name, Address, Phone, Email, Birthday\n" + super().__str__()

    def find_entity(self, text: str) -> List[Contact]:
        return [record for record in self.data if text in record.name.value or text == record.email.value]

    def edit_contact(self, identifier: Union[str, int], field: str, new_value: Any) -> bool:
        contact = None
        
        if isinstance(identifier, int):
            if 0 <= identifier < len(self.data):
                contact = self.data[identifier]
        elif isinstance(identifier, str):
            results = self.find_entity(identifier)
            if results:
                contact = results[0]
        
        if contact:
            if hasattr(contact, field):
                setattr(contact, field, new_value)
                return True
            else:
                raise AttributeError(f"Contact does not have field '{field}'")
        else:
            return False
        
    def delete_contact(self, identifier: Union[str, int]) -> bool:
        if isinstance(identifier, int):
            if 0 <= identifier < len(self.data):
                del self.data[identifier]
                return True
        elif isinstance(identifier, str):
            results = self.find_entity(identifier)
            if results:
                self.data.remove(results[0])
                return True
        return False
