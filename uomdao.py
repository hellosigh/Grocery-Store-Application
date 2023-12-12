from sqlconnection import get_sql_connection

def get_uom(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM uom"
    cursor.execute(query)

    # Initialize an empty list to store response data
    response = []

    # Fetch all rows from the cursor and append them to the response list
    for (uom_id, uom_name) in cursor:
        response.append({
            "uom_id": uom_id,
            "uom_name": uom_name
        })

    return response

if __name__ == '__main__':
    connection = get_sql_connection()

    # Check if the connection is successful before calling get_uom
    if connection is not None:
        print(get_uom(connection))
        connection.close()
