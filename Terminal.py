import os
from FileManager import FileManager
from Fields import *
from Records import *
from Books import *


class Terminal:
    def __init__(self):
        self.contacts_file = FileManager("contacts.csv", "contacts")
        try:
            self.contacts = self.contacts_file.read()
        except FileNotFoundError:
            self.contacts = Contacts()
        self.notes_file = FileManager("notes.csv", "notes")
        try:
            self.notes = self.notes_file.read()
        except FileNotFoundError:
            self.notes = Notes()
        self.call_terminal()

    def call_terminal(self):
        while True:
            user_input = input("Enter a command: ")
            command, args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                self.store_data()
                print("Good bye!")
                break
            elif command == "add-contact":
                print(self.add_contact(*args))
            elif command == "add-note":
                print(self.add_note(*args))
            elif command == "show-contacts":
                print(self.show_contacts())
            elif command == "show-notes":
                print(self.show_notes())
            elif command == "delete-contact":
                print(self.delete_contact(*args))
            elif command == "delete-note":
                print(self.delete_note(*args))
            elif command == "edit-note":
                print(self.edit_note(*args))
            elif command == "find-note":
                print(self.find_note(*args))
            elif command == "add-tag":  
                print(self.add_tag(*args))
            elif command == "delete-tag":
                print(self.delete_tag(*args))
            elif command == "find-note-by-tag":
                print(self.find_note_by_tag(*args))
            elif command == "get-contacts-upcoming-birthdays":
                print(self.show_contacts_with_upcoming_birthdays(*args))
            else:
                print("Invalid command.")

    def parse_input(self, user_input):
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]
        return command, args

    def store_data(self):
        self.contacts_file.write(self.contacts)
        self.notes_file.write(self.notes)

    def add_contact(self, name, address, phone, email, birthday):
        self.contacts.append(Contact(
            Name(name),
            Address(address),
            Phone(phone),
            Email(email),
            Birthday(birthday)
        ))
        return f"Contact '{name}' added successfully."

    def show_contacts(self):
        return str(self.contacts)

    def show_notes(self):
        return str(self.notes)

    def delete_contact(self, name):
        if self.contacts.delete_contact(name):
            return f"Contact '{name}' deleted successfully."
        else:
            return f"Contact '{name}' not found."

    def add_note(self, title, note, tags):
        self.notes.append(Note(
            Title(title),
            Description(note),
            Tags(tags.split(','))
        ))
        return f"Note '{title}' added successfully."    
    
    def delete_note(self, title):
        if self.notes.delete_note(title):
            return f"Note '{title}' deleted successfully."
        else:
            return f"Note '{title}' not found."
    
    def edit_note(self, title, new_title, new_note, new_tags):
        for i, note in enumerate(self.notes.data):
            if note.title.value == title:
                if new_title:
                    note.title.value = new_title
                if new_note:
                    note.note.value = new_note
                if new_tags:
                    note.tags.value = new_tags.split(',')
                return f"Note '{title}' updated successfully."
        return f"Note '{title}' not found."
    
    def find_note(self, text):
        notes = self.notes.find_entity(text)
        if notes:
            return ' \n'.join(str(note) for note in notes)
        else:
            return f"Note with text or title '{text}' not found."

    def add_tag(self, note_title, tag):
        for i, note in enumerate(self.notes.data):
            if note.title.value == note_title:
                note.tags.value.append(tag)
                return f"Tag '{tag}' added to note '{note_title}'."
        return f"Note '{note_title}' not found."

    def delete_tag(self, title, tag):
        for i, note in enumerate(self.notes.data):
            if note.title.value == title:
                if tag in note.tags.value:
                    note.tags.value.remove(tag)
                    return f"Tag '{tag}' removed from note '{title}'."
                else:
                    return f"Tag '{tag}' not found in note '{title}'."
        return f"Note '{title}' not found."
    
    def find_note_by_tag(self, tags):
        notes = self.notes.find_by_tags(tags.split(','))
        if notes:
             return ' \n'.join(str(note) for note in notes)
        else:
            return f"Note with tags '{tags}' not found."
        
    def show_contacts_with_upcoming_birthdays(self, days_from_today):
        contacts = self.contacts.get_contacts_with_upcoming_birthdays(days_from_today)
        if contacts:
            return 'Contacts with upcoming birtdays: ' + '\n'.join(str(contact) for contact in contacts)
        else:
            return f"No upcoming birthdays in {days_from_today} days.."
