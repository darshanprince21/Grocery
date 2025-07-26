from flask import request_finished, request_finished, Response, Flask, request, jsonify
import uom_dao
import sql_connection as connection
import product_dao
import order_dao
import json
# ...existing code...

from flask_cors import CORS
app = Flask(__name__)
CORS(app)



app = Flask(__name__)

connection=connection.get_sql_connection()

@app.route('/getproducts', methods=['GET'])
def get_products():
    products=product_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uoms():
    response=uom_dao.get_uoms(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id=product_dao.delete_product(connection, request.form['product_id'])
    response=jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])  # Parse the JSON string
    order_id = order_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    products=product_dao.get_all_orders(connection)
    response=jsonify(response )
    response.headers.add('Access-Control-Allow-Origin', '*')



@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])  # Parse the JSON string
    product_id = product_dao.insert_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(port=5000, debug=True)  # Set debug=True for development mode
