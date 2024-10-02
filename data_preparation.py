import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect('inventory.db')

    # Load historical sales data (with a new economic conditions field)
    sales_data = pd.read_csv('historical_sales.csv')

    # Insert data into sales_data table
    sales_data.to_sql('sales_data', conn, if_exists='append', index=False)

    conn.close()

def fetch_sales_data():
    conn = sqlite3.connect('inventory.db')
    query = '''
        SELECT * FROM sales_data
    '''
    sales_data = pd.read_sql(query, conn)
    conn.close()
    return sales_data