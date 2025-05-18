class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get) if customer_spending else None

