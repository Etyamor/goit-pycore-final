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

    name = Name("Nikita Kojumyaka")
    address = Address("Odesa, Ukraine")
    phone = Phone("0931234567")
    email = Email("nikita@gmail.com")
    birthday = Birthday("17.11.1996")

    contact2 = Contact(name, address, phone, email, birthday)

    name = Name("Andriy Sviato")
    address = Address("Kyiv, Ukraine")
    phone = Phone("0931234567")
    email = Email("andrii@gmail.com")
    birthday = Birthday("17.11.1996")

    contact3 = Contact(name, address, phone, email, birthday)

    contacts = Contacts()

    contacts.append(contact)
    contacts.append(contact2)
    contacts.append(contact3)

    edited_contact = contacts.edit_contact('Nikita Kojumyaka', 'phone', '0931234000')
    if edited_contact:
        print(f"Contact successfully edited: {edited_contact}")
    else:
        print("Contact not found")

    deleted_contact = contacts.delete_contact('Roma')
    if deleted_contact:
        print(f"Contact successfully deleted: {deleted_contact}")
    else:
        print("Contact not found")


    print("contacts sorted by name: ")
    for con in contacts.sort("name"):
        print(con)


    contacts_file = FileManager("contacts.csv", "contacts")
    contacts_file.write(contacts)
    contacts2 = contacts_file.read()

    print("Data from file:\n" + str(contacts2))
    print("Data from class:\n" + str(contacts))

    title = Title("Title")
    note = Description("Note")
    tags = Tags(["tag1", "tag2", "tag3"])

    note = Note(title, note, tags)

    notes = Notes()

    notes.append(note)
    notes.append(note)
    notes.append(note)

    for nor in notes.find_by_tag(["tag1", "tag2"]):
        print(nor)

    notes_file = FileManager("notes.csv", "notes")
    notes_file.write(notes)
    notes2 = notes_file.read()

    print("Data from class:\n" + str(notes))
    print("Data from file:\n" + str(notes2))


if __name__ == "__main__":
    main()