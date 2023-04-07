from flask import Flask, blueprints, flash, render_template, request, url_for, redirect
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from werkzeug.exceptions import NotFound

import os

from staf.products_form import ProductForm

from models import db, Product

config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__, template_folder="template")
app.config.from_object(f"config.{config_name}")

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)

# @app.cli.command("create-all")
# def command_create_all():
#     with app.app_context():
#         db.create_all()

with app.app_context():
    db.create_all()


def get_product_or_raise(product_id: int) -> Product:
    # db.session.get(Product, product_id)
    product = Product.query.get(product_id)
    if product:
        return product
    raise NotFound(f"Product #{product_id} not found!")


@app.get("/")
def index_view():
    products = db.session.query(Product).all()
    return render_template("index.html", products=products)


@app.get("/about/")
def about_view():
    products = db.session.query(Product).all()
    return render_template("about.html", products=products)

@app.route("/create/", methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("create.html", form=form)

    if not form.validate_on_submit():
        return render_template("create.html", form=form)

    product = Product(
        name = form.data["name"],
        info = form.data["info"]
    )
    db.session.add(product)
    db.session.commit()
    products = db.session.query(Product).all()
    flash(f"Product {product.name} was created!", category="success")
    url = url_for("index_view", products=products)
    return redirect(url)

@app.route("/<int:product_id>/delete/", methods=["GET", "POST"])
def delete_product(product_id: int):
    product = get_product_or_raise(product_id)
    if request.method == "GET":
        return render_template("delete.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Deleted product {product_name}!", category="warning")
    url = url_for("index_view")
    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")