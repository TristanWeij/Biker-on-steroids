class OrderItem:
    def __init__(self, name: str, quantity: int, price: float):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(quantity, int) or not isinstance(price, float):
            raise TypeError

        if quantity <= 0:
            raise RuntimeError('Quantity must be higher than 0!')

        if price <= 0.0:
            raise RuntimeError('Price must be higher than 0.0!')

        self.name = name
        self.quantity = quantity
        self.dailyPrice = price

    def __str__(self):
        return '\n' \
               f'   * Order item: {self.name} \n' \
               f'   * Quantity: {self.quantity} \n' \
               f'   * Price per day: {self.dailyPrice} \n'

    def __repr__(self):
        return str(self)
