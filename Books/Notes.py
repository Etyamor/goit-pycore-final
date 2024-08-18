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
    
    def sort_notes_by_tags(self):
        all_tags = set()
        for note in self.data:
            all_tags.update(note.tags.value)
        
        sorted_tags = sorted(all_tags)
        
        notes_by_tag = {tag: [] for tag in sorted_tags}
        
        for note in self.data:
            if note.tags.value:
                first_tag = sorted(note.tags.value)[0] 
                notes_by_tag[first_tag].append(note)
        
        return notes_by_tag