# connection.py
import pyodbc

def get_connection():
    conn = None
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        print("Connection successful")
    except pyodbc.Error as e:
        print(f"Error accessing database: {e}")
    return conn
