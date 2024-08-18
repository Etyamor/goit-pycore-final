from typing import List
from Books.Book import Book
from Records.Note import Note


class Notes(Book):
    def __str__(self):
        #make good looking format
        header = ['Title', 'Note', 'Tags']
        #make equal length of each column
        max_len = [len(header[0]), len(header[1]), len(header[2])]
        for record in self.data:
            max_len[0] = max(max_len[0], len(record.title.value))
            max_len[1] = max(max_len[1], len(record.note.value))
            max_len[2] = max(max_len[2], len(", ".join(record.tags.value)))
        header = [header[0].ljust(max_len[0]), header[1].ljust(max_len[1]), header[2].ljust(max_len[2])]
        result = " | ".join(header) + "\n"
        result += "-" * (sum(max_len) + 3 * len(max_len) - 2) + "\n"
        for record in self.data:
            result += record.title.value.ljust(max_len[0]) + " | " + record.note.value.ljust(max_len[1]) + " | " + ", ".join(record.tags.value).ljust(max_len[2]) + "\n"
        return result
    
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