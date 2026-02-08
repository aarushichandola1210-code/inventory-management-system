import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ambition21@lpu",   # put your MySQL password here
            database="inventory_db"
        )
        print("MySQL connection successful!")
        return connection

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None


# Run this only to test connection
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        conn.close()
