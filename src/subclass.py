from src.utils import Product, CreationMixin


class Smartphone(Product, CreationMixin):
    """Класс смартфон"""
    def __init__(self, name, description, price, quantity, color, performance, model, memory):
        self.performance = performance
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)

    def new_product(self, *args, **kwargs):
        """Реализация метода new_product"""
        pass


class GrassLawn(Product, CreationMixin):
    """Класс трава газонная"""
    def __init__(self, name, description, price, quantity, color, country, germination_time):
        self.country = country
        self.germination_time = germination_time
        super().__init__(name, description, price, quantity, color)

    def new_product(self, *args, **kwargs):
        """Реализация метода new_product"""
        pass

