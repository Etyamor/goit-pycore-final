import re
from Fields.Field import Field


class Email(Field):
    def __init__(self, value):
        super().__init__(self.validate(value))

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = self.validate(value)

    def validate(self, value):
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not email_regex.match(value):
            raise ValueError("Invalid email address")
        return value
