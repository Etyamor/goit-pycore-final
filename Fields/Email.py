from Fields.Field import Field
import re


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = value 

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not email_regex.match(value):
            raise ValueError("Invalid email address")
        self._value = value