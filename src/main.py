import os

from src.utils import Product, load_data_from_json

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data", "products.json")

categories = load_data_from_json(file_path)
for category in categories:
    print(category.name)
    print(category.description)
    for product in category.get_products():
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)
        print(category.enter_list_products)
        print("####")


product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)

# Устанавливаем новое значение цены с помощью сеттера
product1.price = 90.0
