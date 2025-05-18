import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name_type(self):
        with self.assertRaises(Exception):
            Coffee(123)

    def test_invalid_name_length(self):
        with self.assertRaises(Exception):
            Coffee("Jo")

    def test_name_immutable(self):
        coffee = Coffee("Mocha")
        with self.assertRaises(AttributeError):
            coffee.name = "Espresso"

    def test_coffee_orders(self):
        coffee = Coffee("Americano")
        c = Customer("Tom")
        Order(c, coffee, 4.0)
        Order(c, coffee, 5.0)
        self.assertEqual(len(coffee.orders()), 2)

    def test_coffee_customers(self):
        coffee = Coffee("Cortado")
        c1 = Customer("Amy")
        c2 = Customer("Jake")
        Order(c1, coffee, 3.5)
        Order(c2, coffee, 4.0)
        self.assertEqual(len(coffee.customers()), 2)

    def test_num_orders(self):
        coffee = Coffee("Drip")
        c = Customer("Pam")
        Order(c, coffee, 2.0)
        self.assertEqual(coffee.num_orders(), 1)

    def test_average_price(self):
        coffee = Coffee("Brew")
        c = Customer("Oscar")
        Order(c, coffee, 2.0)
        Order(c, coffee, 4.0)
        self.assertAlmostEqual(coffee.average_price(), 3.0)

if __name__ == "__main__":
    unittest.main()
