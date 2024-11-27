from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
products = []

@app.route('/products', methods=['POST'])
def add_product():
    """Create a new product."""
    try:
        data = request.get_json()
        # Validate input
        if not data or 'name' not in data or 'description' not in data or 'price' not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Create product
        product = {
            "id": len(products) + 1,
            "name": data['name'],
            "description": data['description'],
            "price": float(data['price'])
        }
        products.append(product)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
