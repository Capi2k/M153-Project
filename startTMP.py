from asyncio.windows_events import NULL
import psycopg2
from config import config
from registerDAO import registerDAO

class startDAO():

    def navigateToLogin(self):
        print('login')

    def navigateToRegister(self):
        registerDAO.inputName(registerDAO)


def main():
    strtDAO = startDAO()
    sql = """
            SELECT id FROM gender
            WHERE description = 'M';"""

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

        sqlOutput = cur.fetchall()

        print(cur.fetchall())

        print(1)
        for row in sqlOutput:
            print("output =" , row[0])
        print(2)

        # close communication with the PostgreSQL database server
        print(cur.close())
        # commit the changes
        print(conn.commit())
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    main()