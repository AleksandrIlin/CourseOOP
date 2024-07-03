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

        Category.all_unique_products += len(set([product.name for product in self.__products]))
        Category.all_category += 1

    def __len__(self) -> int:
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт"

    @classmethod
    def set_products(cls, list_products: list) -> None:
        cls.__products = list_products

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

    def __str__(self):
        """Метод для вывода строки"""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для вывода суммы всех товаров на складе"""
        return self._price * self.quantity + other.price * other.quantity

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
                    print("Цена успешно изменена\n")
                else:
                    print(self._price)
                    print("Изменение цены отменено\n")
            else:
                self._price = new_price
                print(self._price)
                print("Цена успешно изменена\n")


class ProductsIterator:
    """Класс итератор по продуктам"""

    def __init__(self, category):
        self.category = category
        self.products = category.get_products()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration()


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
