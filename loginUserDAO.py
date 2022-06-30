from asyncio.windows_events import NULL
from atexit import register
from config import config
import psycopg2
import time
from menuDAO import menuDAO

class loginUserDAO:

    name = ''
    password = ''

    def loginUser(self, name, password):

        self.name = name
        self.password = password


        dbCheckResult = self.checkForUser(self, name, password)

        if(dbCheckResult == 'error'):
            print('User not existing, please register as a user')
            time.sleep(0.5)
        elif(dbCheckResult == 'fuck'):
            print('Uhmmm... we got more than 1 user with this data...')
            time.sleep(0.5)
            print('You have never seen anything...')
            exit(0)
        else:
            menuDAO.menuOptions(menuDAO, self.name, self.password)

    
    def checkForUser(self, name, password):

        sqlGender = """
        SELECT id FROM users
        WHERE name = '{}' AND password = '{}';""".format(name, password)

        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sqlGender)

        if(cur.rowcount == 0):
            result = "error"
        elif(cur.rowcount == 1):
            sqlOutput = cur.fetchall()
            for row in sqlOutput:
                result = row[0]
        else:
            result = 'fuck'

        sqlOutput = cur.fetchall()

        cur.close()
        conn.commit()

        return result

