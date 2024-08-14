from collections import UserList
from typing import List


class Book(UserList):
    def __str__(self) -> str:
        return "\n".join([str(record) for record in self.data])
    
    def find_entity(self, text: str) -> List:
        pass

    def sort(self, key: str, reverse = False) -> List:
        ''' Sorts the data by the key provided '''
        for record in self.data:
            if key not in record.__dict__:
                raise ValueError(f"Key {key} does not exist in {record.__class__.__name__}")
            
        sorted_data = sorted(self.data, key = lambda record: getattr(record, key), reverse = reverse)
        return sorted_data
