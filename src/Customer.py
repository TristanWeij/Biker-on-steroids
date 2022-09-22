class Customer:
    def __init__(self, identifier: int, firstname: str, lastname: str):
        if not isinstance(identifier, int):
            raise TypeError

        if not isinstance(firstname, str) or not isinstance(lastname, str):
            raise TypeError

        self.identifier = identifier
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'ID: {self.identifier} \n' \
               f'Name: {self.full_name()}'

    def full_name(self) -> str:
        return f'{self.firstname} {self.lastname}'
