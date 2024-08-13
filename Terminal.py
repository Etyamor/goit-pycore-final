import datetime
from typing import List
from Books.Contacts import Contacts
from Books.Notes import Notes

class Terminal:
    def __init__(self):
        self.contacts = Contacts()
        self.notes = Notes()
        
        while True:
            user_input = input("Enter a command: ")
            command, args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(self.add_contact(*args))
            elif command == "change":
                print(self.edit_contact(*args))
            elif command == "phone":
                print(self.search_contacts(*args))
            elif command == "all":
                print(self.show_contacts())
            elif command == "add-birthday":
                print(self.add_birthday(*args))
            elif command == "upcoming-birthdays":
                print(self.upcoming_birthdays(int(args[0]) if args else 0))
            elif command == "show-contacts":
                print(self.show_contacts())
            elif command == "show-notes":
                print(self.show_notes())
            elif command == "add-note":
                print(self.add_note(*args))
            elif command == "search-note":
                print(self.search_notes(*args))
            elif command == "search-tag":
                print(self.search_by_tag(*args))
            else:
                print("Invalid command.")

    def add_contact(self, name, address, phone, email, birthday):
        name_field = Name(name)
        address_field = Address(address)
        phone_field = Phone(phone)
        email_field = Email(email)
        birthday_field = Birthday(birthday)

        contact = Contact(name_field, address_field, phone_field, email_field, birthday_field)

        self.contacts.append(contact)

        contacts_file = FileManager("contacts.csv", "contacts")
        contacts_file.write(self.contacts.data)

        return f"Contact '{name}' added and saved successfully."

    def add_note(self, title, note, tags):
        title_field = Title(title)
        description_field = Description(note)
        tags_field = Tags(tags.split(','))

        new_note = Note(title_field, description_field, tags_field)

        self.notes.append(new_note)

        notes_file = FileManager("notes.csv", "notes")
        notes_file.write(self.notes.data)

        return f"Note '{title}' added and saved successfully."

    def delete_contact(self, name):
        contacts_file = FileManager("contacts.csv", "contacts")
        contacts = contacts_file.read()

        for contact in contacts:
            if contact.name.value == name:
                contacts.remove(contact)
                contacts_file.write(contacts)
                return f"Contact '{name}' deleted successfully."

        return f"Contact '{name}' not found."

    def delete_note(self, title):
        notes_file = FileManager("notes.csv", "notes")
        notes = notes_file.read()

        for note in notes:
            if note.title.value == title:
                notes.remove(note)
                notes_file.write(notes)
                return f"Note '{title}' deleted successfully."

        return f"Note '{title}' not found."
    
    def search_contacts(self, name):
        results = self.contacts.find_entity(name)
        if results:
            return "\n".join([f"Name: {contact.name.value}, Address: {contact.address.value}, "
                              f"Phone: {contact.phone.value}, Email: {contact.email.value}, "
                              f"Birthday: {contact.birthday.value}" for contact in results])
        else:
            return f"No contacts found with the name '{name}'."

    def search_notes(self, title):
        results = self.notes.find_entity(title)
        if results:
            return "\n".join([f"Title: {note.title.value}, Description: {note.description.value}, "
                              f"Tags: {', '.join(note.tags.values)}" for note in results])
        else:
            return f"No notes found with the title '{title}'."

    def edit_contact(self, name, phone=None, email=None):
        contacts_file = FileManager("contacts.csv", "contacts")
        contacts = contacts_file.read()

        for contact in contacts:
            if contact.name.value == name:
                if phone:
                    contact.phone = Phone(phone)
                if email:
                    contact.email = Email(email)
                
                contacts_file.write(contacts)
                return f"Contact '{name}' updated successfully."

        return f"Contact '{name}' not found."

    def edit_note(self, title, content=None):
        notes_file = FileManager("notes.csv", "notes")
        notes = notes_file.read()

        for note in notes:
            if note.title.value == title:
                if content:
                    note.description = Description(content)

                notes_file.write(notes)
                return f"Note '{title}' updated successfully."

        return f"Note '{title}' not found."

    def upcoming_birthdays(self, days):
        contacts_file = FileManager("contacts.csv", "contacts")
        contacts = contacts_file.read()
        
        today = datetime.date.today()
        upcoming = []

        for contact in contacts:
            bday = datetime.datetime.strptime(contact.birthday.value, "%Y-%m-%d").date()
            next_birthday = datetime.date(today.year, bday.month, bday.day)
            
            if next_birthday < today:
                next_birthday = datetime.date(today.year + 1, bday.month, bday.day)
            
            if (next_birthday - today).days <= days:
                upcoming.append(f"Name: {contact.name.value}, Birthday: {contact.birthday.value}, Days away: {(next_birthday - today).days}")

        if upcoming:
            return "\n".join(upcoming)
        else:
            return "No upcoming birthdays within the specified range."

    def search_by_tag(self, tag):
        results = [f"Title: {note.title.value}, Description: {note.description.value}, "
                   f"Tags: {', '.join(note.tags.values)}"
                   for note in self.notes.data if tag.lower() in [t.lower() for t in note.tags.values]]

        if results:
            return "\n".join(results)
        else:
            return f"No notes found with the tag '{tag}'."

    def show_contacts(self):
        contacts_file = FileManager("contacts.csv", "contacts")
        contacts = contacts_file.read()

        if not contacts:
            return "No contacts available."

        contacts_info = ""
        for contact in contacts:
            contacts_info += f"Name: {contact.name.value}, Address: {contact.address.value}, " \
                             f"Phone: {contact.phone.value}, Email: {contact.email.value}, " \
                             f"Birthday: {contact.birthday.value}\n"
        
        return contacts_info

    def show_notes(self):
        notes_file = FileManager("notes.csv", "notes")
        notes = notes_file.read()

        if not notes:
            return "No notes available."

        notes_info = ""
        for note in notes:
            notes_info += f"Title: {note.title.value}, Description: {note.description.value}, " \
                          f"Tags: {', '.join(note.tags.values)}\n"
        
        return notes_info

    def parse_input(self, user_input):
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]
        return command, args
