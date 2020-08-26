import mysql.connector

config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)

# Execute queries
cursor = db.cursor()