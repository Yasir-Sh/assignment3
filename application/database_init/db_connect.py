import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    return conn, conn.cursor()

def close_connection(conn, cur):
    conn.close()
    cur.close()