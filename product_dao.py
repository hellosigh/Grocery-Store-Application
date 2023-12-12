from sqlconnection import get_sql_connection

def getAll_product(connection):


    cursor = connection.cursor()

    query = ("select product.product_id,product.name,product.uom_id,product.price_per_unit,uom.uom_name "
             "from product inner join uom on product.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    connection.close()
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    print("Executing Query:", query)
    print("Data:", data)

    cursor.execute(query, data)
    connection.commit()


def Insert_product(connection,product):
    cursor = connection.cursor()
    query =" insert into product(name,uom_id,price_per_unit) values(%s, %s, %s)"
    data= (product['name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM product WHERE product_id = " + str(product_id)
    cursor.execute(query)
    connection.commit()







