from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()

class Product:
    def __init__(self,id,name,price,supplier_id):
        self._id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id




    
    @property
    def id(self):
        return self._id
    @id.setter    
    def id(self, id):
        if not isinstance (id , int):
            raise   TypeError("id must be an integer")
        
        self._id = id


    
    def save(self):
        cursor.execute("SELECT id FROM produst WHERE id = ?", (self._id,))
        if cursor.fetchone():
                raise ValueError(f"Product with id {self._id} already exists")
        sql = """
         INSERT INTO products (
         id, name,price,supplier_id)  
         VALUES (?,?,?,?,?)  
        """
        cursor.execute(sql,(self._id, self.name,self.price,self.supplier_id))
        conn.commit()
    
    @staticmethod   
    def list_products(cursor):
         cursor.execute("""SELECT products.id,products.name,products.price,retailers.name,suppliers.name FROM products
                        LEFT JOIN retailers ON products.retailer_id = retailers.id
                        LEFT JOIN suppliers ON products.supplier_id = suppliers.id""")
         products = cursor.fetchall()
         return products
    @staticmethod
    def delete_product(cursor,id):
         cursor.execute("DELETE FROM products WHERE id = ?",(id,))
         conn.commit()
    @staticmethod
    def product_suppliers(cursor,id):
       sql = """SELECT suppliers.id, suppliers.name FROM suppliers
                INNER JOIN products ON suppliers.id = products.supplier_id
                WHERE products.id = ?"""
       cursor.execute(sql,(id,))
       suppliers  = cursor.fetchall()
       return suppliers
    @staticmethod
    def product_retailers(cursor,id):
       sql = """SELECT retailers.id, retailers.name FROM retailers
                INNER JOIN products ON retailers.id = products.retailer_id
                WHERE products.id = ?"""
       cursor.execute(sql,(id,))
       retailers = cursor.fetchall()
       return retailers
     
    
     



# pilots = Pilot(2,"Mercy",12345,723,1720352227)
# print(pilots._phone_number)