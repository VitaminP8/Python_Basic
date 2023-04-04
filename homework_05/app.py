"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, blueprints, flash, render_template
from dataclasses import dataclass

app = Flask(__name__, template_folder="template")

@dataclass
class Product:
    id: int
    name: str
    info: str = ""

@dataclass()
class ProductStorage:
    products: dict[id, Product]
    last_id: int = 0

    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create(self, name: str) -> Product:
        product = Product(id = self.next_id(), name=name)
        self.products[product.id] = product
        product.info = f"info about product number {product.id} ({product.name})"
        return product

storage = ProductStorage(products={})
storage.create("Phone")
storage.create("Computer")
storage.create("Keys")
storage.create("Book")

@app.get("/")
def index_view():
    products = list(storage.products.values())
    return render_template("index.html", products=products)


@app.get("/about/")
def about_view():
    products = list(storage.products.values())
    return render_template("about.html", products=products)


if __name__ == "__main__":
    app.run(
        debug=True,
    )