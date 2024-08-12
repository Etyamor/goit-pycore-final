from collections import UserList


class Book(UserList):
    def __str__(self):
        return "\n".join([str(record) for record in self.data])
