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

    def add_note(self, title, note, tags):
        self.notes.append(Note(
            Title(title),
            Description(note),
            Tags(tags.split(','))
        ))
        return f"Note '{title}' added successfully."

    def show_contacts(self):
        return str(self.contacts)

    def show_notes(self):
        return str(self.notes)

    def delete_contact(self, name):
        if self.contacts.delete_contact(name):
            return f"Contact '{name}' deleted successfully."
        else:
            return f"Contact '{name}' not found."
