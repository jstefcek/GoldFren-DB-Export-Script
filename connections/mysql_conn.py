# Creates connection to mysql database

# Custom modules
import mysql.connector
import os
from dotenv import load_dotenv

def create_conn():
    """
    Creates connection to MySQL database
    
    Returns:
        conn (connection): MySQL connection
    """
    # Load enviroment variables
    load_dotenv()
    
    # Connect to DB
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    
    # Log
    print('[INFO] - Connection do DB byl vytvoren')
    
    # Return open connection
    return conn