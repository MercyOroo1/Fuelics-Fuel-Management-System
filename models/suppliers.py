from database.connection import get_db_connection
conn = get_db_connection()
cursor = conn.cursor()


class Supplier:
     def __init__(self,id,name,location,certification,rating):
        self._id = id
        self.name = name
        self.location = location
        self.certification = certification
        self.rating = rating
        

        
    
     @property
     def id(self):
        return self._id
     @id.setter    
     def id(self, id):
        if not isinstance (id , int):
            raise   TypeError("id must be an integer")
        
        self._id = id
    
     @property
     def rating(self):
        return self._rating
     @rating.setter    
     def rating(self, rating):
        if not isinstance (rating , int) and len(rating) < 5:
            raise   TypeError("rating must be an integer that is less than 5")
        
        self._rating = rating


   
    
     def save(self):
        cursor.execute("SELECT id FROM suppliers WHERE id = ?", (self._id,))
        if cursor.fetchone():
                raise ValueError(f" Supplier with id {self._id} already exists")
        sql = """
         INSERT INTO suppliers (
          name, location, certification,rating)  
         VALUES (?,?,?,?)  
        """
        cursor.execute(sql,(self._id, self.name,self.location,self.certification,self.rating))
        conn.commit()
     @staticmethod
     def list_suppliers(cursor):
         sql = """
                  SELECT suppliers.id, suppliers.name,suppliers.rating,products.name FROM suppliers
                  LEFT JOIN products ON suppliers.id = products.supplier_id

                  """
         cursor.execute(sql)
         suppliers = cursor.fetchall()
         return suppliers
     @staticmethod
     def delete_suppliers(cursor,id):
         cursor.execute("DELETE FROM suppliers WHERE id = ?",(id,))
         conn.commit()
     
     def supplier_product(self,id):
       sql = """SELECT products.id, products.name FROM products 
                INNER JOIN suppliers ON products.supplier_id = suppliers.id
                WHERE suppliers.id = ?"""
       cursor.execute(sql,(id,))
       product = cursor.fetchall()
       return product
     

     def supplier_retailers(self,id):
       sql = """SELECT retailers.id, retailers.name FROM retailers
                INNER JOIN products ON retailers.id = products.retailer_id
                INNER JOIN suppliers ON products.supplier_id = suppliers.id
                WHERE suppliers.id = ?"""
       cursor.execute(sql,(id,))
       retailers = cursor.fetchall()
       return retailers
     
     @staticmethod
     def find_supplier_by_location(cursor,location):
         sql = """SELECT suppliers.id, suppliers.name FROM suppliers WHERE suppliers.location = ?"""
         cursor.execute(sql,(location,))
         suppliers = cursor.fetchall()
         return suppliers


    

   #   def __repr__(self):
   #      return f'<{self.name}>'
    
     


