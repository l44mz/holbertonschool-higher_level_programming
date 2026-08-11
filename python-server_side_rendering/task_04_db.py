import csv
import json
import sqlite3

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


def read_sql(filename='products.db'):
    """Read and parse product data from a SQLite database."""
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


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

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
    except (FileNotFoundError, sqlite3.Error, json.JSONDecodeError,
            csv.Error) as e:
        return render_template('product_display.html',
                                error=f'Error reading {source} data: {e}')

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
