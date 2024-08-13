from Fields.Field import Field


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits long")
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must be a number")
        if len(value) != 10:
            raise ValueError("Phone number must be 10 digits long")
        self._value = value

    def __str__(self):
        return f"({self._value[:3]}) {self._value[3:6]}-{self._value[6:]}"
