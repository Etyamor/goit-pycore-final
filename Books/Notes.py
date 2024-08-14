from typing import List
from Books.Book import Book
from Records.Note import Note


class Notes(Book):
    def __str__(self):
        return "Title, Note, Tags\n" + super().__str__()
    
    def find_entity(self, text: str) -> List[Note]:
        return [record for record in self.data if text in record.note.value or text in record.title.value]
    
    def find_by_tag(self, tags: List) -> List[Note]:
        result = []
        for record in self.data:
            for tag in tags:
                if tag in record.tags.value:
                    result.append(record)
                    break
                
        return result