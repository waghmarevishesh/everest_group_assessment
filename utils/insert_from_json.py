import json
from connection import connect_db


with open('sample_dataset.json', 'r') as file:
    data = json.load(file)

try:
    connection = connect_db()
    print("Database connection successful")

    with connection:
        with connection.cursor() as cursor:
            for item in data:
                sql = """
                    INSERT INTO projects ( name, description, technologies, image_url)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (item['name'], item['description'], item['technologies'], item['image_url']))
        
        connection.commit()
        print("Data inserted successfully")

except connection.Error as err :
    print(f"Error while inserting {err}")
