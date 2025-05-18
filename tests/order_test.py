import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        customer = Customer("Jim")
        coffee = Coffee("Black")
        order = Order(customer, coffee, 5.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_price_type(self):
        customer = Customer("Pam")
        coffee = Coffee("Green")
        with self.assertRaises(Exception):
            Order(customer, coffee, "5")

    def test_invalid_price_range(self):
        customer = Customer("Dwight")
        coffee = Coffee("Dark")
        with self.assertRaises(Exception):
            Order(customer, coffee, 0.5)

    def test_customer_type(self):
        coffee = Coffee("Roast")
        with self.assertRaises(Exception):
            Order("Angela", coffee, 3.0)

    def test_coffee_type(self):
        customer = Customer("Kevin")
        with self.assertRaises(Exception):
            Order(customer, "Latte", 3.0)

    def test_price_immutable(self):
        customer = Customer("Andy")
        coffee = Coffee("Cold Brew")
        order = Order(customer, coffee, 3.5)
        with self.assertRaises(AttributeError):
            order.price = 4.0

if __name__ == "__main__":
    unittest.main()
