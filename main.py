import sqlite3

def run_sql_examples():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create a sample table: Products
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL
        )
    ''')

    # Insert sample data
    products_data = [
        ('Laptop', 'Electronics', 1200.00),
        ('Smartphone', 'Electronics', 800.00),
        ('Keyboard', 'Accessories', 75.00),
        ('Mouse', 'Accessories', 25.00),
        ('Desk Chair', 'Furniture', 300.00),
        ('Monitor', 'Electronics', 250.00),
        ('Coffee Table', 'Furniture', 150.00),
        ('Webcam', 'Accessories', 60.00)
    ]
    cursor.executemany('INSERT INTO products (name, category, price) VALUES (?, ?, ?)', products_data)
    conn.commit()

    print("--- All Products ---")
    cursor.execute('SELECT name, category, price FROM products')
    for row in cursor.fetchall():
        print(row)
    print("\n")

    # --- Demonstrate SQL IN Operator ---
    print("--- Products in 'Electronics' or 'Furniture' categories (using IN) ---")
    # The IN operator checks if a value matches any value in a list.
    cursor.execute("SELECT name, category, price FROM products WHERE category IN ('Electronics', 'Furniture')")
    for row in cursor.fetchall():
        print(row)
    print("\n")

    # --- Demonstrate SQL NOT IN Operator ---
    print("--- Products NOT in 'Electronics' or 'Furniture' categories (using NOT IN) ---")
    # The NOT IN operator checks if a value does NOT match any value in a list.
    cursor.execute("SELECT name, category, price FROM products WHERE category NOT IN ('Electronics', 'Furniture')")
    for row in cursor.fetchall():
        print(row)
    print("\n")

    # --- Demonstrate IN with a subquery ---
    print("--- Products with price greater than the average price of 'Accessories' (using IN with subquery) ---")
    # A subquery can be used to generate the list for the IN operator.
    cursor.execute("""
        SELECT name, category, price
        FROM products
        WHERE price > (
            SELECT AVG(price) FROM products WHERE category = 'Accessories'
        )
    """)
    for row in cursor.fetchall():
        print(row)
    print("\n")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    run_sql_examples()
