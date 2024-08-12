from Fields.Field import Field


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must be a number")
        if len(value) != 10:
            raise ValueError("Phone number must be 11 digits long")
        self._value = value

    def __str__(self):
        return f"({self._value[:3]}) {self._value[3:6]}-{self._value[6:]}"
