class Order:
    all_orders = []

    def __init__(self, coffee, customer, price):
        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be a Coffee instance.")
