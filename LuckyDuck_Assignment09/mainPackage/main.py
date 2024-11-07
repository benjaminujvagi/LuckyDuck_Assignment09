#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  11/7/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: Connected to a database and ran some queries on it
# Brief Description of what this module does: Grabs everything and prints the sentence


from NewFolder1.module1 import get_connection
from NewFolder2.module2 import get_brand, get_manufacturer, get_products
from NewFolder3.module3 import create_sentence, get_items_sold, select_random_product

import pyodbc




def main():
    conn = get_connection()
    
    cursor = conn.cursor()

    
    products = get_products(cursor)

   
    selected_product = select_random_product(products)
    description = selected_product.Description
    product_id = selected_product.ProductID
    manufacturer_id = selected_product.ManufacturerID
    brand_id = selected_product.BrandID

   
    manufacturer_name = get_manufacturer(cursor, manufacturer_id)

    
    brand_name = get_brand(cursor, brand_id)

    
    number_of_items_sold = get_items_sold(cursor, product_id)

    
    sentence = create_sentence(description, manufacturer_name, brand_name, number_of_items_sold)
    print(sentence)

    
    conn.close()

if __name__ == "__main__":
    main()




