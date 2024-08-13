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
            elif command == "show-birthday":
                print(self.show_birthday(*args))
            elif command == "birthdays":
                print(self.list_birthdays(int(args[0]) if args else 0))
            elif command == "show-contacts":
                print(self.show_contacts())
            elif command == "show-notes":
                print(self.show_notes())
            elif command == "add-note":
                print(self.add_note(*args))
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
        contacts_file.write(self.contacts)

        return f"Contact '{name}' added and saved successfully."

    def add_note(self, title, note, tags):
        title_field = Title(title)
        description_field = Description(note)
        tags_field = Tags(tags.split(','))

        new_note = Note(title_field, description_field, tags_field)

        self.notes.append(new_note)

        notes_file = FileManager("notes.csv", "notes")
        notes_file.write(self.notes)

        return f"Note '{title}' added and saved successfully."
 
    def search_contacts(self, name):

        pass
    
    def search_notes(self, title):
  
        pass
    
    def delete_contact(self, name):

        pass
    
    def delete_note(self, title):
  
        pass
    
    def edit_contact(self, name, phone, email):
 
        pass
    
    def edit_note(self, title, content):

        pass
    
    def list_birthdays(self, days):

        pass
    
    def tag_note(self, title, tag):
  
        pass
    
    def search_by_tag(self, tag):
   
        pass
    
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

terminal = Terminal()

    