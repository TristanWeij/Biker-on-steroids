class Customer:
    def __init__(self, identifier: int, firstname: str, lastname: str, orders=None):
        if not isinstance(identifier, int):
            raise TypeError

        if not isinstance(firstname, str) or not isinstance(lastname, str):
            raise TypeError

        if orders is None:
            self.orders = []
        elif orders is list:
            self.orders = orders
        else:
            raise TypeError

        self.identifier = identifier
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'ID: {self.identifier} \n' \
               f'Name: {self.full_name()} \n' \
               f'Orders: {self.orders}'

    def full_name(self) -> str:
        return f'{self.firstname} {self.lastname}'
