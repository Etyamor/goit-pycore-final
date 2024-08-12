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

    print("Data from class:\n" + str(contacts))

    title = Title("Title")
    note = Description("Note")
    tags = Tags(["tag1", "tag2", "tag3"])

    note = Note(title, note, tags)

    notes = Notes()

    notes.append(note)
    notes.append(note)
    notes.append(note)

    print("Data from class:\n" + str(notes))


if __name__ == "__main__":
    main()
