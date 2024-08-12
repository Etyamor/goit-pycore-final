class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return ", ".join([str(value) for value in self.__dict__.values()])

    def set_record(self, **kwargs):
        self.__dict__.update(kwargs)