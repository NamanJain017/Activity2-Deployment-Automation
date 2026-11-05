import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 1999},
    {"id": 2, "name": "Smart Watch", "price": 2999},
    {"id": 3, "name": "Laptop Backpack", "price": 1499},
]


@app.route("/")
def home():
    products_html = "".join(
        f"<li>{p['name']} - Rs. {p['price']}</li>"
        for p in PRODUCTS
    )

    return f"""
    <html>
      <head><title>ShopEase E-commerce</title></head>
      <body>
        <h1>Welcome to ShopEase</h1>
        <h2>Our Products</h2>
        <ul>{products_html}</ul>
        <p>Application Version: {APP_VERSION}</p>
        <p>Status: Online</p>
        <p>New in version 2.0: Express delivery is now available!</p>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/version")
def version():
    return jsonify(
        application="ShopEase",
        version=APP_VERSION
    ), 200
