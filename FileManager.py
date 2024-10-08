import csv
from Fields import *
from Records import *
from Books import *


class FileManager:
    def __init__(self, file_name:str, data_type:str):
        if file_name.endswith(".csv"):
            self.file_name = file_name
        else:
            raise ValueError("Invalid file extension")
        self.data_type = data_type

    def write(self, data: Contacts | Notes):
        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            # Check if data is Contacts or Notes
            if data.__class__.__name__ == "Contacts":
                fieldnames = ["name", "address", "phone", "email", "birthday"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for contact in data:
                    writer.writerow(contact.__dict__)
            elif data.__class__.__name__ == "Notes":
                fieldnames = ["title", "note", "tags"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for note in data:
                    writer.writerow(note.__dict__)
            else:
                raise ValueError("Invalid data type")

    def read(self) -> Contacts | Notes:
        records = None 
        with open(self.file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Check if file contains contacts or notes
            if self.data_type == "contacts":
                records = Contacts()
                for row in reader:
                    contact = Contact(
                        Name(row["name"]),
                        Address(row["address"]),
                        Phone(''.join(char for char in row["phone"] if char.isdigit())),
                        Email(row["email"]),
                        Birthday(row["birthday"])
                    )
                    records.append(contact)
            elif self.data_type == "notes":
                records = Notes()
                for row in reader:
                    note = Note(
                        Title(row["title"]),
                        Description(row["note"]),
                        Tags(row["tags"].split(", "))
                    )
                    records.append(note)
            else:
                raise ValueError("Invalid file data")
        return records
