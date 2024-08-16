from typing import List, Union, Any, Optional
from datetime import datetime, timedelta
from Books.Book import Book
from Records.Contact import Contact


class Contacts(Book):
    def __str__(self):
        return "Name, Address, Phone, Email, Birthday\n" + super().__str__()

    def find_entity(self, text: str) -> List[Contact]:
        """
        Find contacts by name or email.
        
        :param text: Name or email to search for
        :return: List of matching contacts
        """
        return [record for record in self.data if text in record.name.value or text in record.email.value]

    def edit_contact(self, identifier: Union[str, int], field: str, new_value: Any) -> Optional[Contact]:
        """
        Edit a contact's specified field with a new value.
        
        :param identifier: Name or index of the contact
        :param field: Field to be edited (e.g., 'name', 'address', 'phone', 'email', 'birthday')
        :param new_value: New value for the specified field
        :return: Edited contact if found and modified, None if contact not found
        """
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
                return contact
            else:
                raise AttributeError(f"Contact does not have field '{field}'")
        else:
            return None
        
    def delete_contact(self, identifier: Union[str, int]) -> Optional[Contact]:
        """
        Delete a contact by name or index.
        
        :param identifier: Name or index of the contact
        :return: Deleted contact if found and removed, None if contact not found
        """
        if isinstance(identifier, int):
            if 0 <= identifier < len(self.data):
                contact = self.data.pop(identifier)
                return contact
        elif isinstance(identifier, str):
            results = self.find_entity(identifier)
            if results:
                contact = results[0]
                self.data.remove(contact)
                return contact
        return None

    def get_contacts_with_upcoming_birthdays(self, days_from_today):
        result = Contacts()
        date = datetime.today() + timedelta(days=int(days_from_today))
        for contact in self.data:
            if contact.birthday.value.day == date.day and contact.birthday.value.month == date.month: 
                result.append(contact)
        return result
