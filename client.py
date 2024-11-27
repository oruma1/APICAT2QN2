import requests

BASE_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    """Add a new product."""
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def get_products():
    """Retrieve all products."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to fetch products:", response.json())

# Add products
add_product("Laptop", "A high-performance laptop", 1500.00)
add_product("Phone", "A smartphone with a great camera", 800.00)
add_product("Tablet", "A tablet for reading books", 300.00)
add_product("Smartwatch", "A smartwatch to track your fitness", 200.00)
add_product("Headphones", "Wireless headphones for music", 150.00)
add_product("Keyboard", "A mechanical keyboard for typing", 100.00)

# Fetch all products
get_products()
