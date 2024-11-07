# connection.py
import pyodbc

def get_connection():
    """
    Connect to grocery store database
    """
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
        print("Connection successful")
    except:
        conn = None
    return conn
