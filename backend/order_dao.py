import datetime
from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()
    
    try:
        # Insert into orders table
        order_query = ("INSERT INTO orders (customer_name, total, date_time) VALUES (%s, %s, %s)")
        order_data = (order['customer_name'], order['grand_total'], datetime.now())
        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid

        # Insert into order_details table
        order_detail_query = ("INSERT INTO order_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)")
        order_detail_data = []
        for order_detail_record in order['order_details']:
            order_detail_data.append((
                order_id,
                int(order_detail_record['product_id']),
                float(order_detail_record['quantity']),
                float(order_detail_record['total_price'])
            ))

        cursor.executemany(order_detail_query, order_detail_data)
        connection.commit()
        return order_id
    except Exception as e:
        connection.rollback()
        raise Exception(f"Error inserting order: {str(e)}")
    finally:
        cursor.close()
        
def get_all_products(connection):
        
    cursor =connection.cursor()
    query=("SELECT*FROM  orders")
    cursor.execute(query)
        
    response=[]
    for (order_id, customer_name, total, datetime) in cursor:
        response.append({
            "order_id":order_id,
            "customer_name":customer_name,
            "total":total,
            "datetime": datetime
            })
    return response

      

if __name__ == "__main__":
    try:
        connection = get_sql_connection()
        result = insert_order(connection, {
            'customer_name': "dolly",
            "grand_total": 500,
            "order_details": [
                {
                    'product_id': 10,
                    'quantity': 1,
                    'total_price': 180,
                },
                {
                    'product_id': 22,
                    'quantity': 1,
                    'total_price': 105,
                },
            ]
        })
        print(f"Order inserted with ID: {result}")
    except Exception as e:
        print(f"Failed to insert order: {str(e)}")
    finally:
        if 'connection' in locals():
            connection.close()