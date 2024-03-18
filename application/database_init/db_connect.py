import psycopg2

def connect_to_database():
    #connects to the database running on local host
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )

    #The connection and the cursor object is returned 
    return conn, conn.cursor()

# Closing any open connections and cursors
def close_connection(conn, cur):
    conn.close()
    cur.close()