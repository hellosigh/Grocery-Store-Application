import traceback
from urllib import response

from flask import Flask, request, jsonify, json
from flask_cors import CORS

import product_dao
import uomdao
import order_dao
from sqlconnection import get_sql_connection

app = Flask(__name__)
CORS(app)


# No global connection variable here

@app.route('/getProducts', methods=['GET'])
def get_product():
    # Create a new connection within the function
    connection = get_sql_connection()

    try:
        if connection is None:
            # Handle the case where the connection is not valid
            return jsonify({"error": "Database connection not available"})

        products = product_dao.getAll_product(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow', '*')
        return response
    finally:
        # Close the connection in a 'finally' block to ensure it happens
        if connection is not None:
            connection.close()




# Delete Product_id
@app.route('/getdeleteProduct', methods=['POST'])
def deleteProduct():
    # Create a new connection within the function
    connection = get_sql_connection()

    try:
        if connection is None:
            # Handle the case where the connection is not valid
            return jsonify({"error": "Database connection not available"})

        return_id = product_dao.delete_product(connection, request.form['product_id'])
        response = jsonify(return_id)
        response.headers.add('Access-Control-Allow', '*')
        return response
    finally:
        # Close the connection in a 'finally' block to ensure it happens
        if connection is not None:
            connection.close()


# Corrected placement of getUOM route
@app.route('/getUOM', methods=['GET'])
def get_uom():
    connection = get_sql_connection()

    try:
        response = uomdao.get_uom(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    finally:
        if connection is not None:
            connection.close()
    # Modify the insert_product route


@app.route('/insertProduct', methods=['POST'])

def insert_product():
    try:
        # Ensure the request contains JSON data
        if not request.is_json:
            raise ValueError("Missing JSON data in the request")

        # Parse JSON data from the request body
        request_payload = request.get_json()

        # Print request payload for debugging
        print("Request Payload:", request_payload)

        # Validate the presence of required fields in the JSON data
        required_fields = ['product_name', 'uom_id', 'price_per_unit']
        for field in required_fields:
            if field not in request_payload:
                raise ValueError(f"Missing '{field}' in product data")

        # Create a new connection within the function
        connection = get_sql_connection()

        # Print connection status for debugging
        print("Connection Status:", connection)

        # Call the insert_new_product method from product_dao
        product_id = product_dao.insert_new_product(connection, request_payload)

        # Print the product_id for debugging
        print("Product ID after insertion:", product_id)

        # Create a JSON response with the inserted product_id
        response = jsonify({
            'product_id': product_id
        })

        # Add CORS header to allow cross-origin requests
        response.headers.add('Access-Control-Allow-Origin', '*')

        # Return the JSON response
        return response

    except ValueError as ve:
        # Print detailed error information to the console
        print(f"ValueError: {ve}\n{traceback.format_exc()}")
        return jsonify({'error': str(ve)}), 400  # Bad Request

    except Exception as e:
        # Print detailed error information to the console
        print(f"Error in insert_product: {e}")
        print(traceback.format_exc())
        # Return a 500 Internal Server Error response
        return jsonify({'error': 'Internal Server Error'}), 500

    finally:
        # Close the connection in a 'finally' block to ensure it happens
        if connection is not None:
            connection.close()


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = request.get_json()
    order_id = order_dao.insert_order(order_dao.connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





def hello():
    return "Hello World!"


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(debug=True)


