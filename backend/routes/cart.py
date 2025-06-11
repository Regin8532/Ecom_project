from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection function
def db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='e-com'
    )

# POST: Add product to cart
@app.route('/addtocart', methods=['POST'])
def add_cart():
    data = request.get_json()
    conn = db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO addtocart (id, productname, imageurl, description, price, quantity, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        int(data['id']),
        data['productname'],
        data.get('imageurl'),
        data.get('description'),
        int(data.get('price', 0)),
        int(data.get('quantity', 1)),
        data.get('category')
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Product added to cart', 'id': data['id']}), 201

# GET: Retrieve all products from cart
@app.route('/addtocart', methods=['GET'])
def get_cart():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM addtocart")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    if products:
        return jsonify(products)
    else:
        return jsonify({'message': 'Cart is empty'}), 404

# GET: Retrieve a single product by ID
@app.route('/addtocart/<int:id>', methods=['GET'])
def get_by_id(id):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM addtocart WHERE id = %s", (id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "No such product"}), 404

# PUT: Update a product by ID
@app.route('/addtocart/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    conn = db_connection()
    cursor = conn.cursor()

    query = """
        UPDATE addtocart SET 
            id = %s,
            productname = %s,
            imageurl = %s,
            description = %s,
            price = %s,
            quantity = %s,
            category = %s
        WHERE id = %s
    """

    cursor.execute(query, (
        int(data['id']),
        data['productname'],
        data.get('imageurl'),
        data.get('description'),
        int(data.get('price')),
        int(data.get('quantity')),
        data.get('category'),
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Product updated'}), 200

# DELETE: Delete a product from the cart by ID
@app.route('/addtocart/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM addtocart WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': f'Product with id {id} deleted'}), 200

if __name__ == '_main_':
    app.run(debug=True) 