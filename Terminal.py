class Terminal:
    def __init__(self):
        self.contacts = {}  
        self.notes = {}     
        
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
                print(self.show_all_contacts())
            elif command == "add-birthday":
                print(self.add_birthday(*args))
            elif command == "show-birthday":
                print(self.show_birthday(*args))
            elif command == "birthdays":
                print(self.list_birthdays(int(args[0]) if args else 0))
            else:
                print("Invalid command.")

    def add_contact(self, name, address, phone, email, birthday):
 
        pass
    
    def add_note(self, title, note, tags):

        pass
    
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
    
    def list_birthdays(self):

        pass
    
    def tag_note(self, title, tag):
  
        pass
    
    def search_by_tag(self, tag):
   
        pass

terminal = Terminal()

    