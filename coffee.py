class Coffee:
    def __init__(self, name)
        if ininstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Coffee name must be a string with at least 3 characters.")