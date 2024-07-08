from src.utils import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory



class GrassLawn(Product):
    def __init__(self, name, description, price, quantity, color, country, germination_time):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_time = germination_time

