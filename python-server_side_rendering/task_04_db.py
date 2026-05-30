from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# JSON
def read_json():
    with open('products.json') as f:
        return json.load(f)


# CSV
def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


# SQL (SQLite)
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception as e:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    data = []

    # SOURCE SELECTION
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

    else:
        return render_template("product_display.html",
                               products=[],
                               error="Wrong source")

    # ID filter
    if id_param:
        id_param = int(id_param)
        filtered = [p for p in data if p['id'] == id_param]

        if not filtered:
            return render_template("product_display.html",
                                   products=[],
                                   error="Product not found")

        data = filtered

    return render_template("product_display.html",
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
