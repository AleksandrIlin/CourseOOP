import json
import os
from typing import Any

import pytest
from src.utils import Category, Product, ProductsIterator, load_data_from_json


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
    assert category_object.get_products() == [product1, product2]
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
    """тест проверяющий что обьект не пустой"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data", "products.json")
    result = load_data_from_json(file_path)
    assert len(result) > 0


def test_category():
    # Создаем тестовые продукты
    product1 = Product("Яблоко", "Сладкое яблоко", 50.0, 10)
    product2 = Product("Груша", "Сочная груша", 70.0, 5)
    product3 = Product("Апельсин", "Сочный апельсин", 80.0, 15)

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


def test_product():
    # Создаем тестовый продукт
    product = Product("Яблоко", "Сладкое яблоко", 50.0, 10)

    # Проверяем атрибуты продукта
    assert product.name == "Яблоко"
    assert product.description == "Сладкое яблоко"
    assert product._price == 50.0
    assert product.quantity == 10
    assert str(product) == "Яблоко, 50.0 руб. Остаток: 10 шт."

    # Проверяем работу геттера и сеттера для цены
    assert product.price == 50.0
    product.price = 60.0
    assert product._price == 60.0
    # Не пытаемся установить цену ниже 0
    # product.price = 40.0


def test_load_data_from_json():
    # Создаем тестовый файл JSON
    test_data = [
        {
            "name": "Фрукты",
            "description": "Различные фрукты",
            "products": [
                {"name": "Яблоко", "description": "Сладкое яблоко", "price": 50.0, "quantity": 10},
                {"name": "Груша", "description": "Сочная груша", "price": 70.0, "quantity": 5},
                {"name": "Апельсин", "description": "Сочный апельсин", "price": 80.0, "quantity": 15},
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


def test_str_method():
    product = Product("Apple", "Fruits", 10.0, 5)
    assert str(product) == "Apple, 10.0 руб. Остаток: 5 шт."


def test_add_method():
    product1 = Product("Apple", "Fruits", 10, 5)
    product2 = Product("Orange", "Fruits", 15.0, 3)
    total_value = product1 + product2
    assert total_value == 95.0


@pytest.fixture
def category():
    products = [
        Product("Product 1", "Description 1", 10.0, 5),
        Product("Product 2", "Description 2", 15.0, 3),
        Product("Product 3", "Description 3", 20.0, 2),
    ]
    return Category("Test Category", "Description", products)


def test_products_iterator(category):
    products_iterator = ProductsIterator(category)
    assert len(list(products_iterator)) == 3


def test_products_iterator_next(category):
    products_iterator = ProductsIterator(category)
    product1 = next(products_iterator)
    assert product1.name == "Product 1"
    product2 = next(products_iterator)
    assert product2.name == "Product 2"
    product3 = next(products_iterator)
    assert product3.name == "Product 3"
    with pytest.raises(StopIteration):
        next(products_iterator)


def test_products_iterator_iteration(category):
    products_iterator = ProductsIterator(category)
    products = [product for product in products_iterator]
    assert len(products) == 3
    assert products[0].name == "Product 1"
    assert products[1].name == "Product 2"
    assert products[2].name == "Product 3"
