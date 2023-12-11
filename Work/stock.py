class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if self.shares - nshares < 0:
            raise ValueError(f"Cannot sell {nshares} shares when you only hold {self.shares}")
        self.shares -= nshares

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()

    def panic(self):
        self.sell(self.shares)
