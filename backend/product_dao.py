import mysql.connector
from sql_connection import get_sql_connection
def get_all_products(connection):
        
        cursor =connection.cursor()
        query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit,uom.uom_name FROM "
                "products INNER JOIN uom ON products.uom_id = uom.uom_id;")
        cursor.execute(query)
        # an empty array to hold the products
        response = []

        for (product_id,name, uom_id,price_per_unit,uom_name) in cursor:
            response.append({
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            })
            
            
       
        return response
    
 # This function inserts a new product into the products table
# It takes a connection object and a product dictionary as parameters   
def insert_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    
    data=(product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid
#lastrowid returns the id of the last inserted row

# This function updates an existing product in the products table
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id =" +str(product_id))
    cursor.execute(query)
    connection.commit()
     


if __name__ == "__main__":
    connection= get_sql_connection()
    print(delete_product(connection, 16))