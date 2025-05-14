import pymysql.cursors
import logging

def connect_db():
    try:
        logging.info("attempting db connecttion")

        connection = pymysql.connect(host='localhost',
                    user='root',
                    password='28317100',
                    database='showcase_db',
                    cursorclass=pymysql.cursors.DictCursor)
        logging.info("DB connection successful")
        return connection
        
     
    except pymysql.connect.Error as err:
        logging.error(f"error on DB connection {str(err)}")

