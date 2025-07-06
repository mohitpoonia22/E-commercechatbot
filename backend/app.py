from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy product data (for testing)
products = [
    {"name": "Red Shirt", "price": 499, "description": "A stylish red shirt for all seasons"},
    {"name": "Bluetooth Headphones", "price": 999, "description": "Wireless and noise cancelling"},
    {"name": "Running Shoes", "price": 1299, "description": "Comfortable for daily use"},
    {"name": "Smart Watch", "price": 2199, "description": "Track your fitness and receive calls"},
    {"name": "Backpack", "price": 799, "description": "Spacious and durable for college use"}
]

@app.route('/')
def home():
    return "ShopMate AI Backend is Running ✅"

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()

    # Filter products based on name or description
    matching = [
        item for item in products
        if query in item['name'].lower() or query in item['description'].lower()
    ]

    return jsonify(matching)

if __name__ == '__main__':
    app.run(debug=True)
