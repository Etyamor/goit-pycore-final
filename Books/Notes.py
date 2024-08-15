from typing import List
from Books.Book import Book
from Records.Note import Note


class Notes(Book):
    def __str__(self):
        return "Title, Note, Tags\n" + super().__str__()
    
    def find_entity(self, text: str) -> List[Note]:
        return [record for record in self.data if text in record.note.value or text in record.title.value]
    
    def find_by_tags(self, tags: List) -> List[Note]:
        result = []
        for note in self.data:
            for tag in tags:
                if tag in note.tags.value:
                    result.append(note)
                    break
                
        return result
    
    def delete_note(self, title: str):
        for i, record in enumerate(self.data):
            if record.title.value == title:
                del self.data[i]
                return True  
        return False  