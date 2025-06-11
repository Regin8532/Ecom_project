from flask import Flask, request, jsonify
from flask import send_from_directory, Blueprint
from flask_cors import CORS
import mysql.connector



app = Flask(__name__)
CORS(app)  # 👈 Add this line


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ecom'
    )

# Create a product
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO products (name, price, stock, image, description)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['name'],
        data['price'],
        data.get('stock', 0),
        data.get('image'),
        data.get('description')
    ))
    conn.commit()
    product_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'message': 'Product created', 'product_id': product_id}), 201

# Get all products
# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    # Add full image URL
    for product in products:
        if product.get('image'):
            product['image_url'] = f"http://127.0.0.1:5000/static/images/{product['image']}"

    return jsonify(products)


# Get a product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product:
        if product.get('image'):
            product['image_url'] = f"http://127.0.0.1:5000/static/images/{product['image']}"
        return jsonify(product)

    return jsonify({'error': 'Product not found'}), 404

# Update a product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE products SET name=%s, price=%s, stock=%s, image=%s, description=%s
        WHERE id=%s
    """
    cursor.execute(query, (
        data['name'],
        data['price'],
        data['stock'],
        data.get('image'),
        data.get('description'),
        product_id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Product updated'})

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Product deleted'})

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    response = send_from_directory('static/images', filename)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)