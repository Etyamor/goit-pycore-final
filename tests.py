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

from FileManager import FileManager


def main():
    name = Name("Maksym Rutkovskyi")
    address = Address("Lviv, Ukraine")
    phone = Phone("0931234567")
    email = Email("maxikrud0071@gmail.com")
    birthday = Birthday("17.11.1996")

    contact = Contact(name, address, phone, email, birthday)

    contacts = Contacts()

    contacts.append(contact)
    contacts.append(contact)
    contacts.append(contact)


    contacts_file = FileManager("contacts.csv")
    contacts_file.write(contacts)
    contacts2 = contacts_file.read()

    print("Data from class:\n" + str(contacts))
    print("Data from file:\n" + str(contacts2))

    title = Title("Title")
    note = Description("Note")
    tags = Tags(["tag1", "tag2", "tag3"])

    note = Note(title, note, tags)

    notes = Notes()

    notes.append(note)
    notes.append(note)
    notes.append(note)

    notes_file = FileManager("notes.csv")
    notes_file.write(notes)
    notes2 = notes_file.read()

    print("Data from class:\n" + str(notes))
    print("Data from file:\n" + str(notes2))


if __name__ == "__main__":
    main()
