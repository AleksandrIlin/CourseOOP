import os

from src.utils import Product, ProductsIterator, load_data_from_json
from src.subclass import Smartphone, GrassLawn

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data", "products.json")

categories = load_data_from_json(file_path)
for category in categories:
    print(category.name)
    print(category.description)
    print(category)  # Вывод количество продуктов категории ДЗ 15_1
    for product in category.get_products():
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
        print(product)
        print("####")
    print()


product1 = Product("Товар 1", "Описание товара 1", 100.0, 10, "цвет")

# Устанавливаем новое значение цены с помощью сеттера
product1.price = 90.0

product2 = Product("Товар 2", "Описание товара 2", 200.0, 20, "цвет")

total_price = product1 + product2  # подсчет суммы всех продуктов на складе ДЗ15_1
print(f"Общая сумма продуктов на складе: {total_price}\n")

# Дополнительное задание к ДЗ 15_1
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data", "products.json")
categories = load_data_from_json(file_path)

for category in categories:
    print(f"Категория: {category.name}")
    category_products = ProductsIterator(category)
    for product in category_products:
        print(f"{product.name} - {product.price}")
    print()


smartphone1 = Smartphone("iPhone 12", "Смартфон фирмы Apple", 60000, 10, "Черный",
                         4.5, "iPhone 12", 128)
smartphone2 = Smartphone("Samsung Galaxy S21", "Смартфон фирмы Samsung", 50000, 15,
                         "Белый", 4.8, "Galaxy S21", 256)

grass_lawn1 = GrassLawn("Газонная трава", "трава для газона", 500, 10, "Зеленый",
                        "Россия", 14)
product1 = Product("Книга", "для чтения", 300, 5, "Канцелярия")

print(f"Сумма класса смартфон - {smartphone1 + smartphone2}\n")  # iPhone 12 - 110000 руб.
print(f"Сумма класса трава газонная - {grass_lawn1 + grass_lawn1}\n")  # Газонная трава - 1000 руб.

try:
    print(smartphone1 + product1)
except TypeError as e:
    print(f"Вывод ошибки при сложении разных классов - {e}")  # Можно складывать только одинаковые типы продуктов


# products_list = Product.create_and_add_to_list([], "Test Product", "Test Description",
#                                                10.0, 0, "Red")

products_list = Product.create_and_add_to_list([], "Test Product", "Test Description",
                                               10.0, "5", "Red")
