import psycopg2

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="customers",
        user="postgres",
        password="postgres")

connect