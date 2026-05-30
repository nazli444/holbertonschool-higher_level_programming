from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# JSON oxuma
def read_json():
    with open('products.json') as f:
        return json.load(f)


# CSV oxuma
def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    data = []
    error = None

    # SOURCE yoxlama
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    # ID filter
    if id_param:
        id_param = int(id_param)
        filtered = [p for p in data if p['id'] == id_param]

        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])

        data = filtered

    return render_template("product_display.html", products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
