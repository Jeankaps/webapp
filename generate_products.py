import csv
import random
from datetime import datetime

# List of electronic product names
product_names = [
    "Smartphone",
    "Laptop",
    "Tablet",
    "Smartwatch",
    "Headphones",
    "Bluetooth Speaker",
    "Camera",
    "TV",
    "Gaming Console",
    "Router",
    "External Hard Drive",
    "Monitor",
    "Printer",
    "Fitness Tracker",
    "Drone",
    "E-book Reader",
    "Smart Home Device"
]

# Sample descriptions
descriptions = [
    "High-performance device with advanced features.",
    "Sleek and portable design, perfect for on-the-go use.",
    "Enhanced connectivity and seamless integration with other devices.",
    "Immersive audio and video experience.",
    "Cutting-edge technology for superior performance.",
    "Easy setup and user-friendly interface.",
    "Long battery life and fast charging capabilities.",
    "Durable construction for long-lasting use."
]

# Generate products
products = []
sql_statements = []

for i in range(100):
    name = random.choice(product_names)
    description = random.choice(descriptions)
    price = round(random.uniform(50, 2000), 2)  # Random price between $50 and $2000
    quantity = random.randint(1, 100)  # Random quantity between 1 and 100
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = created_at
    products.append((name, description, price, quantity, created_at, updated_at))

    # Generate SQL statement
    sql = f"INSERT INTO Product (name, description, price, quantity, created_at, updated_at) VALUES "
    sql += f"('{name}', '{description}', {price}, {quantity}, '{created_at}', '{updated_at}');"
    sql_statements.append(sql)

# Write SQL statements to file
with open('insert_products.sql', 'w') as sql_file:
    for statement in sql_statements:
        sql_file.write(statement + '\n')

print("SQL statements generated successfully.")
