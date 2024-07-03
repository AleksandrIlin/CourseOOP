import os

from src.utils import Product, ProductsIterator, load_data_from_json

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


product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)

# Устанавливаем новое значение цены с помощью сеттера
product1.price = 90.0

product2 = Product("Товар 2", "Описание товара 2", 200.0, 20)

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
        print(product.name, product.price)
    print()
