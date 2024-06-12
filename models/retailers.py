from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()

class Retailer:
     def __init__(self,id,name,phone,town,region,manager):
        self._id = id
        self.name = name
        self.phone= phone
        self.town = town
        self.region = region
        self.manager = manager
        

    
     @property
     def id(self):
        return self._id
     @id.setter    
     def id(self, id):
        if not isinstance (id , int):
            raise   TypeError("id must be an integer")
        
        self._id = id

   
    
     def save(self):
        cursor.execute("SELECT id FROM retailers WHERE id = ?", (self._id,))
        if cursor.fetchone():
                raise ValueError(f"Retailer with id {self._id} already exists")
        sql = """
         INSERT INTO flights (
         id, name, phone, town, region, manager)  
         VALUES (?,?,?,?,?,?)  
        """
        cursor.execute(sql,(self._id, self.name,self.phone,self.town,self.region,self.manager))
        conn.commit()

     @staticmethod
     def list_retailers(self):
         cursor.execute("""SELECT retailers.id,retailers.name,retailers.phone,retailers.town,retailers.region,retailers.manager,products.id FROM retailers 
                        LEFT JOIN products ON retailers.id = products.retailer_id
                       """)
         retailers = cursor.fetchall()
         return retailers
     
     @staticmethod
     def delete_retailers(cursor,id):
         cursor.execute("DELETE FROM retailers WHERE id = ?",(id,))
         conn.commit()

     @staticmethod
     def assign_retailer_to_product(cursor, retailers_id, product_id):
       if Retailer.retailer_exists(cursor, retailers_id):
        if Retailer.product_exists(cursor, product_id):
         cursor.execute("""UPDATE products SET retailer_id = ? WHERE id = ?""",
                       (retailers_id, product_id))
         conn.commit()
         print(f"Retailer {retailers_id} assigned to product {product_id}.")
        else: 
          print(f"Product with ID {product_id} does not exist.")
       else:
         print(f"Retailer with ID {retailers_id} does not exist.")

     @staticmethod
     def retailer_exists(cursor, retailer_id):
       cursor.execute("""SELECT * FROM retailers WHERE id = ?""", (retailer_id,))
       return cursor.fetchone() is not None
     
     @staticmethod
     def product_exists(cursor, product_id):
        cursor.execute("""SELECT * FROM products WHERE id = ?""", (product_id,))
        return cursor.fetchone() is not None
     
     @staticmethod
     def retailer_suppliers(cursor,id):
        sql = """SELECT suppliers.id, suppliers.name FROM suppliers
                  INNER JOIN products ON suppliers.id = products.supplier_id
                  INNER JOIN retailers ON products.retailer_id = retailers.id
                   WHERE retailers.id = ? """
        cursor.execute(sql,(id,))
        suppliers = cursor.fetchall()
        return suppliers
     
     
     @staticmethod
     def retailers_products(cursor,id):
         sql = """SELECT products.id, products.name FROM products
                  INNER JOIN retailers ON products.retailer_id = retailers.id
                  WHERE retailers.id = ?"""
         cursor.execute(sql,(id,))
         products = cursor.fetchall()
         return products
      
     @staticmethod
     def find_retailer_by_town(cursor,town):
         sql = """SELECT retailers.id, retailers.name FROM retailers WHERE retailers.town = ?"""
         cursor.execute(sql,(town,))
         retailers = cursor.fetchall()
         return retailers
     

# flight = Flight(2,"KQ",12345,"Sweden",1)
# print(flight.flight_name)