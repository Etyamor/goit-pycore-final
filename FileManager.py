import csv
from Fields.Name import Name
from Fields.Address import Address
from Fields.Phone import Phone
from Fields.Email import Email
from Fields.Birthday import Birthday
from Records.Contact import Contact
from Books.Contacts import Contacts

from Fields.Title import Title
from Fields.Description import Description
from Fields.Tags import Tags
from Records.Note import Note
from Books.Notes import Notes

class FileManager:
    def __init__(self, file_name:str):
        if file_name.endswith(".csv"):
            self.file_name = file_name

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
            if "birthday" in reader.fieldnames:
                records = Contacts()
                for row in reader:
                    contact = Contact(
                        Name(row["name"]),
                        Address(row["address"]),
                        Phone(row["phone"]),
                        Email(row["email"]),
                        Birthday(row["birthday"])
                    )
                    records.append(contact)
            elif "tags" in reader.fieldnames:
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