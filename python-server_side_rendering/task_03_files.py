import csv
import json

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename='products.json'):
    """Read and parse product data from a JSON file."""
    with open(filename) as f:
        return json.load(f)


def read_csv(filename='products.csv'):
    """Read and parse product data from a CSV file."""
    products = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    items_list = data.get('items', []) if isinstance(data, dict) else []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html', error='Wrong source')

    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                    error='Product not found')

        product = next((p for p in data if p['id'] == product_id), None)
        if product is None:
            return render_template('product_display.html',
                                    error='Product not found')
        return render_template('product_display.html', products=[product])

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
