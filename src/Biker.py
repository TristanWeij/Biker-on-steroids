from src.Customer import Customer
from src.Order import Order
from src.OrderItem import OrderItem


class Biker:
    @staticmethod
    def create_order(customer: Customer, items: list[OrderItem]) -> Order:
        customer_order = Order(customer, items)
        customer.orders.append(customer_order)

        return customer_order
