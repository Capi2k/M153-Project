from asyncio.windows_events import NULL
from config import config
import psycopg2


# several where statements
# https://stackoverflow.com/questions/8645773/sql-query-with-multiple-where-statements


class updateDataDAO:

    # I need to get the username and the password in order to search 
    # for the right data. These values will be delivered after the login.
    # Means I need to wait a bit
    
    def updateData(self, column, value, recognizeValue):
        sql = """
                UPDATE users
                SET {}={}
                WHERE {};""".format(column, value, recognizeValue)

        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # create table one by one
            cur.execute(sql)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')