from src.Customer import Customer
from src.Biker import Biker
from src.OrderItem import OrderItem

if __name__ == '__main__':
    customer = Customer(1, 'Tristan', 'Weij')

    orderItems = [
        OrderItem('Rode herenfiets', 1, 25.0),
        OrderItem('Kinderzitje', 1, 5.0),
        OrderItem('Helm', 2, 3.5)
    ]

    customerOrder = Biker.create_order(customer, orderItems)

    print(customer)

    print('test')
