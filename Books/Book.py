from collections import UserList
from typing import List

class Book(UserList):
    def __str__(self) -> str:
        return "\n".join([str(record) for record in self.data])
    
    def find_entity(self, text: str) -> List:
        pass
