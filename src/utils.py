import json
import os
from typing import Any


class Category:
    """Класс категория"""

    name: str
    description: str
    products: list
    all_category = 0
    all_unique_products = 0

    def __init__(self, name: Any, description: Any, products: Any) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self.products = products

        Category.all_unique_products += len(set([product.name for product in products]))
        Category.all_category += 1


class Product:
    """Класс продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> Any:
        return (
            f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
        )


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data", "products.json")


def load_data_from_json(file_path: str) -> Any:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        categories = []
        for category_data in data:
            name = category_data["name"]
            description = category_data["description"]
            products_data = category_data["products"]
            products = []
            for product_data in products_data:
                product = Product(
                    product_data["name"], product_data["description"], product_data["price"], product_data["quantity"]
                )
                products.append(product)
            category = Category(name, description, products)
            categories.append(category)
        return categories


categories = load_data_from_json(file_path)
for category in categories:
    print(category.name)
    print(category.description)
    for product in category.products:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
