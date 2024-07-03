import os
import unittest
from typing import Any
from unittest.mock import patch

import pytest
from src.utils import Category, Product, load_data_from_json


@pytest.fixture
def product1() -> Any:
    return Product("топ", "для занятия спортом", 599, 10)


@pytest.fixture
def product2() -> Any:
    return Product("топ2", "для занятия спортом2", 599, 10)


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
    assert category_object._Category__products == [product1, product2]
    assert category_object.all_category == 1
    assert category_object.all_unique_products == 2


@pytest.fixture
def product_object() -> Any:
    """Тест получает на вход класс Product для удобства дальнейшей работы"""
    return Product("Одежда", "для занятия спортом", 599, 10)


def test_init_product(product_object: Any) -> None:
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product_object.name == "Одежда"
    assert product_object.description == "для занятия спортом"
    assert product_object.price == 599
    assert product_object.quantity == 10


def test_load_data_from_file() -> None:
    """Тест проверяющий, что объект не пустой"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data", "products.json")
    result = load_data_from_json(file_path)
    assert len(result) > 0


@pytest.fixture
def sample_category() -> Any:
    return Category("Electronics", "Category for electronic devices", [])


@pytest.fixture
def sample_product_list() -> list:
    return [Product("Laptop", "Powerful laptop", 1500, 10), Product("Phone", "Smartphone", 800, 20)]


def test_category_initialization(sample_category: Any) -> None:
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Category for electronic devices"
    assert sample_category.all_category == 4


def test_product_initialization(sample_product_list: list) -> None:
    assert len(sample_product_list) == 2
    assert sample_product_list[0].name == "Laptop"
    assert sample_product_list[1].quantity == 20
    assert Category.all_unique_products == 6


def test_product_creation(sample_product_list: list) -> None:
    new_product = Product.create_and_add_to_list(sample_product_list, "Laptop", "New powerful laptop", 1700, 5)
    assert new_product.quantity == 15
    assert len(sample_product_list) == 2


def test_category_init() -> None:
    category = Category("Electronics", "Electronic devices", [])
    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert category.get_products() == []


# Тестирование класса Product
def test_product_init() -> None:
    product = Product("Laptop", "Powerful laptop", 1000, 5)
    assert product.name == "Laptop"
    assert product.description == "Powerful laptop"
    assert product._price == 1000
    assert product.quantity == 5


def test_price_getter() -> None:
    product = Product("товар", "описание", 100, 10)
    assert product.price == 100


def test_price_setter() -> None:
    product = Product("товар", "описание", 100, 10)
    product._price = 90
    assert product.price == 90


def test_price_setter_negative() -> None:
    product = Product("товар", "описание", 100, 10)
    product.price = -10
    assert product.price == 100


def test_enter_list_products() -> None:
    product = Product("товар", "описание", 100, 10)
    category = Category("категория", "описание категории", [product])
    assert category.enter_list_products == "категория, 100руб. Остаток: 10"


class TestProduct(unittest.TestCase):
    def test_price_setter(self) -> None:
        product = Product("Товар", "Описание", 10.0, 5)
        with patch("builtins.input", return_value="yes"):  # перехватываем вызов функции input
            product.price = 8.0
        self.assertEqual(product.price, 8.0)

    def test_price(self) -> None:
        product = Product("Товар", "Описание", 10.0, 5)
        with patch("builtins.input", return_value="no"):  # перехватываем вызов функции input
            product.price = 6.0
        self.assertEqual(product.price, 10.0)
