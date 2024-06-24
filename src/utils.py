import json
import os


class Category:
    """ Класс категория"""
    name: str
    description: str
    products: list
    all_category = 0
    all_unique_products = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self.products = products

        Category.all_unique_products += len(set([product.name for product in products]))
        Category.all_category += 1


class Product:
    """ Класс продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f'Product(name={self.name}, description={self.description},'
                f'price={self.price}, quantity={self.quantity})')


def load_data_from_file():
    """Загрузка данных из файла .json"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data", "products.json")
    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)
    for product in data:
        products_list = []
        for prod in product['products']:
            products_list.append(Product(prod['name'], prod['description'], prod['price'], product['quantity']))
        Category(product['name'], product['description'], products_list)
