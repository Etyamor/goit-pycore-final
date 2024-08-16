from Fields.Field import Field


class Phone(Field):
    def __init__(self, value):
        super().__init__(self.validate(value))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.validate(value)

    def __str__(self):
        return f"({self._value[:3]}) {self._value[3:6]}-{self._value[6:]}"

    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits long")
        return value
