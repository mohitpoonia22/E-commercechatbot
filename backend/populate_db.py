import sqlite3
import random

# Connect to database (or create it)
conn = sqlite3.connect('products.db')
c = conn.cursor()

# Create table with all required fields
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_url TEXT,
        stock INTEGER
    )
''')

# Sample data for generating random products
categories = ["Electronics", "Books", "Fashion", "Toys", "Home", "Fitness"]
product_names = {
    "Electronics": ["Mouse", "Keyboard", "Headphones", "Webcam", "Monitor"],
    "Books": ["Python 101", "AI Future", "Mystery Novel", "Space Explained", "Mind Hacks"],
    "Fashion": ["T-shirt", "Sneakers", "Hoodie", "Sunglasses", "Jeans"],
    "Toys": ["Lego Set", "RC Car", "Puzzle", "Rubik Cube", "Action Figure"],
    "Home": ["Mug", "Lamp", "Wall Clock", "Cushion", "Curtain"],
    "Fitness": ["Yoga Mat", "Dumbbells", "Treadmill", "Skipping Rope", "Water Bottle"]
}

# Insert 100+ products
for _ in range(120):
    category = random.choice(categories)
    name = random.choice(product_names[category]) + f" {random.randint(101, 999)}"
    price = round(random.uniform(200, 5000), 2)
    description = f"This is a premium quality {name.lower()} for your daily use."
    image_url = f"https://via.placeholder.com/150?text={name.replace(' ', '+')}"
    stock = random.randint(5, 50)

    c.execute('''
        INSERT INTO products (name, category, price, description, image_url, stock)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, price, description, image_url, stock))

# Save and close
conn.commit()
conn.close()
print("✅ Database populated with 120 sample products.")
