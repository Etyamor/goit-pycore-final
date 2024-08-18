from typing import List, Union, Any, Optional
from datetime import datetime, timedelta
from Books.Book import Book
from Records.Contact import Contact


class Contacts(Book):
    def __str__(self):
        header = ['Name', 'Address', 'Phone', 'Email', 'Birthday']
        max_len = [len(header[0]), len(header[1]), len(header[2]), len(header[3]), len(header[4])]
        for record in self.data:
            max_len[0] = max(max_len[0], len(record.name.value))
            max_len[1] = max(max_len[1], len(record.address.value))
            max_len[2] = max(max_len[2], len(record.phone.value))
            max_len[3] = max(max_len[3], len(record.email.value))
            max_len[4] = max(max_len[4], len(str(record.birthday)))
        header = [header[0].ljust(max_len[0]), header[1].ljust(max_len[1]), header[2].ljust(max_len[2]),
                  header[3].ljust(max_len[3]), header[4].ljust(max_len[4])]
        result = " | ".join(header) + "\n"
        result += "-" * (sum(max_len) + 3 * len(max_len) - 2) + "\n"
        for record in self.data:
            result += record.name.value.ljust(max_len[0]) + " | " + record.address.value.ljust(max_len[1]) + " | " + \
                      record.phone.value.ljust(max_len[2]) + " | " + record.email.value.ljust(max_len[3]) + " | " + \
                      str(record.birthday).ljust(max_len[4]) + "\n"
        return result

    def find_entity(self, text: str) -> List[Contact]:
        return [record for record in self.data if text in record.name.value or text in record.email.value]

    def edit_contact(self, identifier: Union[str, int], field: str, new_value: Any) -> Optional[Contact]:
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
