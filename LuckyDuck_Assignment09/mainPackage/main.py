#main.py


from NewFolder1 import *
from NewFolder2 import *
from NewFolder3 import *

def main():
    conn = get_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    # Step 1: Fetch products
    products = fetch_products(cursor)

    # Step 2: Select a random product
    selected_product = select_random_product(products)
    description = selected_product.Description
    product_id = selected_product.ProductID
    manufacturer_id = selected_product.ManufacturerID
    brand_id = selected_product.BrandID

    # Step 3: Fetch manufacturer name
    manufacturer_name = fetch_manufacturer(cursor, manufacturer_id)

    # Step 4: Fetch brand name
    brand_name = fetch_brand(cursor, brand_id)

    # Step 5: Fetch number of items sold
    number_of_items_sold = fetch_number_of_items_sold(cursor, product_id)

    # Step 6: Build and print the sentence
    sentence = build_sentence(description, manufacturer_name, brand_name, number_of_items_sold)
    print(sentence)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()




