from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""  
            CREATE TABLE IF NOT EXISTS retailers (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  phone INTEGER NOT NULL,
                  town TEXT NOT NULL,
                  region TEXT NOT NULL,
                  manager TEXT NOT NULL
                  
                  
                  )

       
                  """)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location  TEXT NOT NULL,
            certification TEXT NOT NULL,
            rating INT NOT NULL
                 
                   
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            supplier_id INTEGER NOT NULL,
            retailer_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
            FOREIGN KEY (retailer_id) REFERENCES retailers(id)  
                      
                   
        )
    ''')
 