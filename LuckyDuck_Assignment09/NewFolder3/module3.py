#Generate sentence

import random

def get_items_sold(cursor, product_id):
    query = f"""
    SELECT SUM(QtyOfProduct) AS ItemsSold
    FROM dbo.tTransactionDetail
    JOIN dbo.tTransaction ON tTransactionDetail.TransactionID = tTransaction.TransactionID
    WHERE tTransaction.TransactionTypeID = 1 AND tTransactionDetail.ProductID = {product_id}
    """
    cursor.execute(query)
    return cursor.fetchone().ItemsSold or 0  # Returns 0 if no items are sold

def select_random_product(products):
    return random.choice(products)

def create_sentence(description, manufacturer, brand, items_sold):
    return f"The product '{description}', manufactured by '{manufacturer}' under the '{brand}' brand, has sold {items_sold} items."
