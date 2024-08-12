from Fields.Field import Field


class Tags(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return ', '.join(self._value)

