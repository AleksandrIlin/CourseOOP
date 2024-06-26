import os
from typing import Any

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
    assert category_object.products == [product1, product2]
    assert category_object.all_category == 3
    assert category_object.all_unique_products == 6


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
    """тест проверяющий что обьект не пустой"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data", "products.json")
    result = load_data_from_json(file_path)
    assert len(result) > 0
