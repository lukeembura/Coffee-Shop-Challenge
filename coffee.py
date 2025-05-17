class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Coffee name must be a string with at least 3 characters.")
        
    @property
    def name(self):
        return self._name
    
    def  orders(self):
        return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    