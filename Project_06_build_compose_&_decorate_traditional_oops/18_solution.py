class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter        
    def price(self, value):
        print("Setting price...")
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative.")
        
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)

p.price = -2
print(p.price)

del p.price