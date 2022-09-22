from src.Customer import Customer


def create_customer(customer_id: int) -> Customer:
    customer_first_name = input('Enter your first name: ')
    customer_last_name = input('Enter your last name: ')

    return Customer(customer_id, customer_first_name, customer_last_name)


if __name__ == '__main__':
    customers = []

    print('\033[94m******> Welcome to Biker! <******\033[0m')

    for i in range(1, 6):
        customer = create_customer(i)
        customers.append(customer)

        print(f'\n\033[94mINFO: Customer created! \033[0m\n')

    print(customers)
