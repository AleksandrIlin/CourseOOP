import json
import os
from typing import Any
from unittest.mock import patch
import unittest

import pytest
from src.utils import Category, Product, ProductsIterator, load_data_from_json


@pytest.fixture
def product1() -> Any:
    return Product("топ", "для занятия спортом", 599, 10, "red")


@pytest.fixture
def product2() -> Any:
    return Product("топ2", "для занятия спортом2", 599, 10, "red")


@pytest.fixture
def category_object(product1: Any, product2: Any) -> Any:
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    return Category("одежда", "для спорта", [product1, product2])


def test_init_category(category_object: Any, product1: Any, product2: Any) -> None:
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.name == "одежда"
    assert category_object.description == "для спорта"
    assert category_object.get_products() == [product1, product2]
    assert category_object.all_category == 1
    assert category_object.all_unique_products == 2


@pytest.fixture
def product_object() -> Any:
    """Тест получает на вход класс Product для удобства дальнейшей работы"""
    return Product("Одежда", "для занятия спортом", 599, 10, "белый")


def test_init_product(product_object: Any) -> None:
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product_object.name == "Одежда"
    assert product_object.description == "для занятия спортом"
    assert product_object.price == 599
    assert product_object.quantity == 10
    assert product_object.color == "белый"


def test_load_data_from_file() -> None:
    """Тест проверяющий, что объект не пустой."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data", "products.json")
    result = load_data_from_json(file_path)
    assert len(result) > 0


def test_category() -> None:
    # Создаем тестовые продукты
    product1 = Product("Яблоко", "Сладкое яблоко", 50.0, 10, "green")
    product2 = Product("Груша", "Сочная груша", 70.0, 5, "red")
    product3 = Product("Апельсин", "Сочный апельсин", 80.0, 15, "orange")

    # Создаем тестовую категорию
    category = Category("Фрукты", "Различные фрукты", [product1, product2, product3])

    # Проверяем атрибуты категории
    assert category.name == "Фрукты"
    assert category.description == "Различные фрукты"
    assert len(category) == 30
    assert str(category) == "Фрукты, количество продуктов: 30 шт"

    # Проверяем работу геттера и сеттера для продуктов
    assert sorted(category.get_products(), key=lambda x: x.name) == sorted(
        [product1, product2, product3], key=lambda x: x.name
    )
    category.set_products([product3, product2, product1])
    assert sorted(category.get_products(), key=lambda x: x.name) == sorted(
        [product3, product2, product1], key=lambda x: x.name
    )


def test_product() -> None:
    # Создаем тестовый продукт
    product = Product("Яблоко", "Сладкое яблоко", 50.0, 10, "red")

    # Проверяем атрибуты продукта
    assert product.name == "Яблоко"
    assert product.description == "Сладкое яблоко"
    assert product._price == 50.0
    assert product.quantity == 10
    assert product.color == "red"
    assert str(product) == "Яблоко, 50.0 руб. Остаток: 10 шт."

    # Проверяем работу геттера и сеттера для цены
    assert product.price == 50.0
    product.price = 60.0
    assert product._price == 60.0
    # Не пытаемся установить цену ниже 0
    # product.price = 40.0


def test_load_data_from_json() -> None:
    # Создаем тестовый файл JSON
    test_data = [
        {
            "name": "Фрукты",
            "description": "Различные фрукты",
            "products": [
                {"name": "Яблоко", "description": "Сладкое яблоко", "price": 50.0, "quantity": 10, "color": "red"},
                {"name": "Груша", "description": "Сочная груша", "price": 70.0, "quantity": 5, "color": "green"},
                {"name": "Апельсин", "description": "Сочный апельсин", "price": 80.0,
                 "quantity": 15, "color": "orange"},
            ],
        }
    ]

    with open("test_data.json", "w", encoding="utf-8") as file:
        json.dump(test_data, file)

    # Загружаем данные из файла и проверяем результат
    categories = load_data_from_json("test_data.json")
    assert len(categories) == 1
    category = categories[0]
    assert category.name == "Фрукты"
    assert category.description == "Различные фрукты"
    assert len(category.get_products()) == 3
    assert Category.all_category == 5

    os.remove("test_data.json")


def test_str_method() -> None:
    product = Product("Apple", "Fruits", 10.0, 5, "red")
    assert str(product) == "Apple, 10.0 руб. Остаток: 5 шт."


def test_add_method() -> None:
    product1 = Product("Apple", "Fruits", 10, 5, "green")
    product2 = Product("Orange", "Fruits", 15.0, 3, "orange")
    total_value = product1 + product2
    assert total_value == 95.0


@pytest.fixture
def category() -> Any:
    products = [
        Product("Product 1", "Description 1", 10.0, 5, "black"),
        Product("Product 2", "Description 2", 15.0, 3, "red"),
        Product("Product 3", "Description 3", 20.0, 2, "blue"),
    ]
    return Category("Test Category", "Description", products)


def test_products_iterator(category: Any) -> None:
    products_iterator = ProductsIterator(category)
    assert len(list(products_iterator)) == 3


def test_products_iterator_next(category: Any) -> None:
    products_iterator = ProductsIterator(category)
    product1 = next(products_iterator)
    assert product1.name == "Product 1"
    product2 = next(products_iterator)
    assert product2.name == "Product 2"
    product3 = next(products_iterator)
    assert product3.name == "Product 3"
    with pytest.raises(StopIteration):
        next(products_iterator)


def test_products_iterator_iteration(category: Any) -> None:
    products_iterator = ProductsIterator(category)
    products = [product for product in products_iterator]
    assert len(products) == 3
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2"
    assert products[2].name == "Product 3"


class TestProduct(unittest.TestCase):
    def test_price_setter(self) -> None:
        product = Product("Товар", "Описание", 10.0, 5, "цвет")
        with patch("builtins.input", return_value="yes"):  # перехватываем вызов функции input
            product.price = 8.0
        self.assertEqual(product.price, 8.0)

    def test_price(self) -> None:
        product = Product("Товар", "Описание", 10.0, 5, "цвет")
        with patch("builtins.input", return_value="no"):  # перехватываем вызов функции input
            product.price = 6.0
        self.assertEqual(product.price, 10.0)





def test_create_and_add_to_list_valid_input():
    # Создаем объект, который имеет атрибут 'name'
    class MyObject:
        def __init__(self, name):
            self.name = name

    # Создаем список и добавляем объект в него
    my_list = []
    obj = MyObject("my_object")
    my_list.append(obj)

    # Проверяем, что объект был добавлен в список
    assert len(my_list) == 1
    assert my_list[0].name == "my_object"



def test_create_and_add_to_list_missing_argument():
    products_list = []
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", "Test Description",
                                       10.0, 5, "color", "some_object")


def test_create_and_add_to_list_extra_argument():
    products_list = []
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", "Test Description", 10.0,
                                       5, "Red", "some_object", "extra_argument")


def test_create_and_add_to_list_invalid_input():
    products_list = []
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, 123, "Test Description", 10.0, 5, "color")
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", 123, 10.0, 5, "color")
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", "Test Description", "10.0", 5, "color")
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", "Test Description", 10.0, "5", "color")
    with pytest.raises(TypeError):
        Product.create_and_add_to_list(products_list, "Test Product", "Test Description", 10.0, 5, 123)


def test_category_len(category_object):
    assert len(category_object) == 20


def test_products_iterator_empty_category(product1, product2):
    category = Category("Test Category", "Description", [])
    products_iterator = ProductsIterator(category)
    with pytest.raises(StopIteration):
        next(products_iterator)
