#query.py

def get_products(cursor):
    cursor.execute("SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID FROM tProduct")
    return cursor.fetchall()

def get_manufacturer(cursor, manufacturer_id):
    cursor.execute(f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}")
    return cursor.fetchone()[0]

def get_brand(cursor, brand_id):
    cursor.execute(f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}")
    return cursor.fetchone()[0]