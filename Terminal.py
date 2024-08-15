import shlex
from prompt_toolkit import prompt
from AutoCompleter import AutoCompleter
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

        self.commands = {
            "add-contact": ("Add a new contact with 5 arguments", 5),
            "add-note": ("Add a new note with 3 arguments", 3),
            "show-contacts": ("Show all contacts with no arguments", 0),
            "show-notes": ("Show all notes with no arguments", 0),
            "delete-contact": ("Delete a contact by name with 1 argument", 1),
            "delete-note": ("Delete a note by title with 1 argument", 1),
            "edit-note": ("Edit a note by title with 4 arguments", 4),
            "find-note": ("Find a note by text or title with 1 argument", 1),
            "find-note-by-tag": ("Find a note by tag with 1 argument", 1),
            "add-tag": ("Add a tag to a note by title with 2 arguments", 2),
            "delete-tag": ("Delete a tag from a note by title with 2 arguments", 2),
            "get-contacts-upcoming-birthdays": ("Get contacts with upcoming birthdays with 1 argument", 1),
            "close": ("Exit the program with no arguments", 0),
            "exit": ("Exit the program with no arguments", 0),
            "help": ("Display available commands with no arguments", 0)
        }
        self.auto_completer = AutoCompleter(list(self.commands.keys()))

        self.call_terminal()

    def display_commands(self):
        print("Available commands:")
        for command, (description, _) in self.commands.items():
            print(f"{command}: {description}")

    def call_terminal(self):
        self.display_commands()
        while True:
            user_input = prompt(
                "Enter a command: ",
                completer=self.auto_completer.get_completer(),
                complete_while_typing=False
            )
            command, args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                self.store_data()
                print("Good bye!")
                break
            elif command == "help":
                self.display_commands()
            else:
                self.execute_command(command, args)

    def execute_command(self, command, args):
        if command not in self.commands:
            print("Invalid command.")
            return

        description, expected_args = self.commands[command]
        try:
            if len(args) != expected_args:
                raise ValueError(f"'{command}' requires {expected_args} arguments, but {len(args)} were provided.")

            if command == "add-contact":
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
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")

    def parse_input(self, user_input):
        parts = shlex.split(user_input)
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

    def find_note_by_tag(self, tags):
        notes = self.notes.find_by_tags(tags.split(','))
        if notes:
             return ' \n'.join(str(note) for note in notes)
        else:
            return f"Note with tags '{tags}' not found."

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
        
    def show_contacts_with_upcoming_birthdays(self, days_from_today):
        contacts = self.contacts.get_contacts_with_upcoming_birthdays(days_from_today)
        if contacts:
            return 'Contacts with upcoming birtdays:\n' + str(contacts)
        else:
            return f"No upcoming birthdays in {days_from_today} days.."
