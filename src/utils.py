import json
from typing import Any
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс"""
    @abstractmethod
    def new_product(self, *args, **kwargs):
        """Абстрактный метод"""
        pass


class CreationMixin:
    """Класс миксин"""

    def __init__(self, *args, **kwargs):
        """Инициализация класса миксин"""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        """Вывод для разработчика"""
        return f"Создан объект класса {self.__class__.__name__}: {self}"


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
        """Получение суммы продуктов в категории"""
        return sum(product.quantity for product in self.__products)

    def __str__(self) -> str:
        """Вывод количество продуктов в категории"""
        return f"{self.name}, количество продуктов: {len(self)} шт"

    @classmethod
    def set_products(cls, list_products: list) -> None:
        """Получение списка продуктов"""
        cls.__products = list_products

    def get_products(self) -> list:
        """Получение приватного продукта"""
        return self.__products


class Product(BaseProduct, CreationMixin):
    """Класс продукт"""
    name: str
    description: str
    _price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, *args, **kwargs) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self.color = color
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        """Метод для вывода строки"""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения товаров одного класса"""
        if isinstance(other, self.__class__):
            result = self._price * self.quantity + other.price * other.quantity
            return result
        else:
            raise TypeError("Можно складывать только товары одного класса")

    def new_product(self, *args, **kwargs):
        """Реализация метода new_product"""
        pass

    @classmethod
    def create_and_add_to_list(
            cls, products_list: list, name: str, description: str, price: float, quantity: int, color: str) -> Any:
        """Метод для создания товара и добавления его в список товаров с проверкой наличия дубликата."""
        for product in products_list:
            if product.name == name:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product

        # Проверяем, что объект является экземпляром класса Product или его наследником
        if (not isinstance(name, str) or not isinstance(description, str)
                or not isinstance(price, float) or not isinstance(quantity, int) or not isinstance(color, str)):
            raise TypeError("Неверный тип данных для создания продукта")

        new_product = cls(name, description, price, quantity, color)
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

    def __init__(self, category: Any) -> None:
        self.category = category
        self.products = category.get_products()
        self.index = 0

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> Any:
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
                    product_data["name"], product_data["description"], product_data["price"], product_data["quantity"],
                    product_data["color"]
                )
                products.append(product)
            category = Category(name, description, products)
            categories.append(category)
        return categories
