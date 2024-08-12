from Records.Record import Record


class Note(Record):
    def __init__(self, title, note, tags):
        super().__init__(title=title, note=note, tags=tags)
