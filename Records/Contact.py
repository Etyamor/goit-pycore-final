from Records.Record import Record


class Contact(Record):
    def __init__(self, name, address, phone, email, birthday):
        super().__init__(name=name, address=address, phone=phone, email=email, birthday=birthday)
