import json
from typing import Any


class Category:
    """Класс категория"""

    name: str
    description: str
    __products: list
    all_category = 0
    all_unique_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self.__products = products  # изменение атрибута на приватный

        Category.all_unique_products += len(set([product.name for product in products]))
        Category.all_category += 1

    @classmethod
    def set_products(cls, list_products: list) -> None:
        cls.__products = list_products

    @property
    def enter_list_products(self) -> str:
        product = self.__products[0]  # Получаем первый продукт из списка
        return f"{self.name}, {product.price} руб. Остаток: {product.quantity}"

    def get_products(self) -> list:
        return self.__products


class Product:
    """Класс продукт"""

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_and_add_to_list(
        cls, products_list: list, name: str, description: str, price: float, quantity: int
    ) -> Any:
        """Метод для создания товара и добавления его в список товаров с проверкой наличия дубликата."""
        for product in products_list:
            if product.name == name:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product
        new_product = cls(name, description, price, quantity)
        products_list.append(new_product)
        return products_list

    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута цены."""
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            if new_price < self._price:
                user_input = input("Вы уверены, что хотите понизить цену? (yes/no): ")
                if user_input.lower() in ["y", "yes", "да"]:
                    self._price = new_price
                    print(self._price)
                    print("Цена успешно изменена")
                else:
                    print(self._price)
                    print("Изменение цены отменено")
            else:
                self._price = new_price
                print(self._price)
                print("Цена успешно изменена")


def load_data_from_json(file_path: str) -> Any:
    """Функция чтения file.json"""
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
