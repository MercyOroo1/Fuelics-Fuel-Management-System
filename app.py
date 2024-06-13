from database.setup import create_tables
from database.connection import get_db_connection
from models.products import Product
from models.suppliers import Supplier
from models.retailers import Retailer
conn= get_db_connection()
cursor = conn.cursor()
def main():
    create_tables()
    # conn= get_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("""DROP TABLE suppliers""")
    # conn.commit()

    while True:
        print("\n1. Add record")
        print("2. List all suppliers")
        print("3. List all retailers")
        print("4. List all products")
        print("5. Assign product to a retailer")
        print("6. Get product supplied by a specific supplier")
        print("7. Get retailer served by a specific supplier")
        print("8. Get supplier that supply a specific product")
        print("9. Get retailers that supply a specific product")
        print("10. Get suppliers that supply a specific retailer")
        print("11. Get products that are supplied by a specific retailer")
        print("12. Find supplier by location")
        print("13. Find retailer by town")
        print("14. Delete records")
        print("15.Exit")
        choice = input("Enter choice: ")

        conn = get_db_connection()
        cursor = conn.cursor()
        
        if choice == "1":
                    while True:
                        print("\n1. Add supplier and product")
                        print("2. Add retailer")
                        print("3. Exit")
                
                        choice = input("Enter choice: ")
                        if choice == "1":
                         suppliers_name = input ("Enter suppliers name: ")
                         suppliers_location = input("Enter suppliers location: ")
                         suppliers_certification = input("Enter suppliers certication: ")
                         suppliers_ratings = int(input("Enter suppliers ratings: "))
                         product_name = input("Enter products name: ")
                         product_price = input("Enter products price: ")
                        

                        
                         cursor.execute('INSERT INTO suppliers (name,location,certification,rating) VALUES (?,?,?,?)', (suppliers_name,suppliers_location,suppliers_certification,suppliers_ratings))
                         supplier_id = cursor.lastrowid
                         cursor.execute('INSERT INTO products (name,price,supplier_id) VALUES (?,?,?)', (product_name,product_price,supplier_id))

                         conn.commit()
                      
                        elif choice == "2":
                         retailers_name = input("Enter retailers name: ")
                         retailers_phone=input("Enter retailers phone number: ")
                         retailers_town = input("Enter the town where the retailer is located: ")
                         retailers_region = input("Enter the region where the retailer is located: ")
                         retailers_manager = input("Enter the retailers manager: ")  
                         cursor.execute('INSERT INTO retailers (name,phone,town,region,manager) VALUES (?,?,?,?,?)',(retailers_name,retailers_phone,retailers_town,retailers_region,retailers_manager))
                         conn.commit()
                        elif choice == "3":
                            print("Exiting")
                            break
                        else:
                         print("Invalid option. Please enter a valid option.")
                        
                        

        elif choice == "2":
            suppliers = Supplier.list_suppliers(cursor)
            for supplier in suppliers:
               print(f"Supplier ID:{supplier[0]}, Supplier name:{supplier[1]}, Suppliers rating:{supplier[2]}, Products name:{supplier[3]}")
        
        elif choice == "3":
            retailers = Retailer.list_retailers(cursor)
            for retailer in retailers:
               print(f"Retailer ID:{retailer[0]},Retailer Name:{retailer[1]}, Retailers phone:{retailer[2]}, town:{retailer[3]}, region:{retailer[4]}, manager:{retailer[5]}, product:{retailer[6]}")
        elif choice == "4":
            products = Product.list_products(cursor)
            for product in products:
               print(f"Products ID:{product[0]},Product Name:{product[1]}, Product Price:{product[2]}, Retailers Name:{product[3]}, Supplier Name:{product[4]}")
        elif choice == "5":
            product = int(input("Enter products ID: "))
            retailer = int(input("Enter retailer ID: "))
            Retailer.assign_retailer_to_product(cursor,retailer,product)
            conn.commit()
        elif choice == "6":
           supplier_id = int(input("Enter supplier ID: "))
           products = Supplier.supplier_product(cursor, supplier_id)
           for product in products:
            if product is not None:
             print(f"Supplier {supplier_id} supplies Product ID:{product[0]}, Product Name:{product[1]}")
            else:
             print("No supplier found for the product.")
        elif choice == "7":
           supplier_id = int(input("Enter Supplier ID: "))
           retailers = Supplier.supplier_retailers(cursor,supplier_id)
           for retailer in retailers:
            if retailer is not None:
               print(f"Supplier {supplier_id} supplies Retailer ID:{retailer[0]}, Retailer Name:{retailer[1]}")
        
        elif choice == "8":
           product_id = int(input("Enter product ID: "))
           suppliers = Product.product_suppliers(cursor,product_id)
           if not suppliers:
              print("There are no suppliers for this product")
           else:
              for supplier in suppliers:
                 print(f"Product {product_id} is supplied by Supplier ID: {supplier[0]}, Supplier Name: {supplier[1]}")
            
        elif choice == "9":
            product_id = int(input("Enter product ID: "))
            retailers = Product.product_retailers(cursor,product_id)
            if not retailers:
               print("There are no retailers for this product")
            else:
             for retailer in retailers:
                 print(f"Product {product_id} is supplied by Retailer ID: {retailer[0]},Retailers Name: {retailer[1]}")
             
        elif choice == "10":
           retailer_id = int(input("Enter Retailer ID: "))
           suppliers = Retailer.retailer_suppliers(cursor,retailer_id)
          
           if not suppliers:
              print ("Retailer is not supplied by any retailer")
           else:
              for supplier in suppliers:
                print(f"Retailer {retailer_id} is supplied by Supplier ID: {supplier[0]}, Supplier Name: {supplier[1]}")
             
        elif choice == "11":
            retailer_id = int(input("Enter Retailer ID: "))
            products = Retailer.retailers_products(cursor,retailer_id)
            if not products:
                 print ("Retailer does not sell any product")
            else:
                 for product in products:
                  print(f"Retailer {retailer_id} is sells  Product ID: {product[0]}, Product Name: {product[1]}")
        elif choice == "12":
            suppliers_location = input("Enter supplier location: ")
            suppliers = Supplier.find_supplier_by_location(cursor,suppliers_location)
            if not suppliers:
             print("No suppliers in this location")
            else:
             for supplier in suppliers:
               print(f"Supplier ID: {supplier[0]}, Supplier's Name: {supplier[1]}")
  
            
        elif choice == "13":
           
           retailers_town = input("Enter retailer town: ")
           retailers = Retailer.find_retailer_by_town(cursor, retailers_town)
    
           if not retailers:
            print("No retailers in this location")
           else:
             for retailer in retailers:
               print(f"Retailer ID: {retailer[0]}, Retailer's Name: {retailer[1]}")
  
            
        elif choice == "14":
           


              while True:
                        print("\n1. Delete Suppliers")
                        print("2. Delete Products")
                        print("3. Delete retailers")
                        print("4. Exit")
                        choice = input("Enter choice: ")
                        if choice == "1":
                           id = int(input("Enter Supplier ID: "))
                           Supplier.delete_suppliers(cursor,id)
                           conn.commit()
                           print(f"Supplier {id} has been deleted")

                        
                         
                      
                        elif choice == "2":
                          id = int(input("Enter Product ID: "))
                          Product.delete_product(cursor,id)
                          conn.commit()
                          print(f"Product {id} has been deleted")
                         
                        elif choice == "3":
                             id = int(input("Enter Retailer ID: "))
                             Retailer.delete_retailers(cursor,id)
                             conn.commit
                             print(f"Retailer {id} has been deleted")
                        elif choice == "4":
                            print("Exiting")
                            break
                        else:
                         print("Invalid option. Please enter a valid option.")
        elif choice == "15":
           print ("exiting")
           break
        else:
          print("Invalid option. Please enter a valid option.")
    

      



                
             
       
           
           
           
            
                     
                      
                  
                 
           
           

          

           


if __name__ == "__main__":
    main()
