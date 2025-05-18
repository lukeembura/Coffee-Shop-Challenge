import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("John")
        self.assertEqual(c.name, "John")

    def test_invalid_name_type(self):
        with self.assertRaises(Exception):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(Exception):
            Customer("J" * 20)

    def test_customer_orders(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        o1 = Order(c, coffee, 3.0)
        o2 = Order(c, coffee, 4.0)
        self.assertEqual(len(c.orders()), 2)

    def test_customer_coffees(self):
        c = Customer("Bob")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        Order(c, coffee1, 3.0)
        Order(c, coffee2, 4.0)
        self.assertEqual(len(c.coffees()), 2)

    def test_create_order(self):
        c = Customer("Dana")
        coffee = Coffee("Flat White")
        order = c.create_order(coffee, 4.5)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)

    def test_most_aficionado(self):
        c1 = Customer("Max")
        c2 = Customer("Sam")
        coffee = Coffee("Cappuccino")
        c1.create_order(coffee, 5.0)
        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 3.0)
        self.assertEqual(Customer.most_aficionado(coffee), c1)

if __name__ == "__main__":
    unittest.main()
