import sqlite3

def create_tables():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create inventory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            current_stock INTEGER,
            adjusted_stock INTEGER
        )
    ''')

    # Create sales data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_data (
            date TEXT,
            product_id INTEGER,
            sales INTEGER,
            price REAL,
            economic_conditions TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()