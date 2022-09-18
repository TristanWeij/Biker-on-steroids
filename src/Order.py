from src.Customer import Customer
from src.OrderItem import OrderItem


class Order:
    def __init__(self, customer: Customer, items: list[OrderItem]):
        if not isinstance(customer, Customer) or not isinstance(items, list):
            raise TypeError

        self.customer = customer
        self.orderItems = items

    def __str__(self):
        return f'Order geplaatst door: {self.customer.full_name()} \n' \
               f'Items: {self.orderItems}'

    def __repr__(self):
        return str(self)

    def total_price(self) -> float:
        price = 0.0

        for orderItem in self.orderItems:
            if not isinstance(orderItem, OrderItem):
                raise TypeError

            price += orderItem.dailyPrice * orderItem.quantity

        return price
