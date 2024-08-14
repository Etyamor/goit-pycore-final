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
            "close": ("Exit the program with no arguments", 0),
            "exit": ("Exit the program with no arguments", 0),
            "help": ("Display available commands with no arguments", 0)
        }
        
        self.call_terminal()

    def display_commands(self):
        print("Available commands:")
        for command, (description, _) in self.commands.items():
            print(f"{command}: {description}")

    def call_terminal(self):
        self.display_commands()  
        while True:
            user_input = input("Enter a command: ")
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
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An error occurred: {e}")
