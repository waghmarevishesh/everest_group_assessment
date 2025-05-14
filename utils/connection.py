import pymysql.cursors
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_db():
    try:
        logging.info("attempting db connecttion")

        connection = pymysql.connect(host='localhost',
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'),
                        database=os.getenv('DB_NAME'),
                        cursorclass=pymysql.cursors.DictCursor)
        logging.info("DB connection successful")
        return connection
        
     
    except pymysql.connect.Error as err:
        logging.error(f"error on DB connection {str(err)}")

