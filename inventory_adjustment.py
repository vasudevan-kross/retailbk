import sqlite3

def adjust_inventory(predictions, product_ids):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    for product_id, predicted_sales in zip(product_ids, predictions):
        cursor.execute('SELECT current_stock FROM inventory WHERE product_id = ?', (product_id,))
        current_stock = cursor.fetchone()[0]

        # Calculate new stock level
        adjusted_stock = current_stock - predicted_sales

        # Update the inventory table
        cursor.execute('UPDATE inventory SET adjusted_stock = ? WHERE product_id = ?', (adjusted_stock, product_id))

    conn.commit()
    conn.close()
