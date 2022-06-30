from asyncio.windows_events import NULL
from config import config
import psycopg2


# several where statements
# https://stackoverflow.com/questions/8645773/sql-query-with-multiple-where-statements


class updateDataDAO:

    # I need to get the username and the password in order to search 
    # for the right data. These values will be delivered after the login.
    # Means I need to wait a bit

    name = ''
    password = ''
    
    def updateData(self, setColumn, newValue, whereColumn1, recognizeValue, whereColumn2, recognizeValue2):

        self.name = recognizeValue
        self.password = recognizeValue2

        sql = ''

        if(setColumn == 'gender' or setColumn == 'preference'):
            genderValue = self.getGenderFKValue(self, newValue)
            sql = """
                UPDATE users
                SET {}='{}'
                WHERE {}='{}' AND {}='{}';""".format(setColumn, genderValue, whereColumn1, recognizeValue, whereColumn2, recognizeValue2)
        elif(setColumn == 'nationality'):
            nationalityValue = self.getNationalityFKValue(self, newValue)
            sql = """
                UPDATE users
                SET {}='{}'
                WHERE {}='{}' AND {}='{}';""".format(setColumn, nationalityValue, whereColumn1, recognizeValue, whereColumn2, recognizeValue2)
        else:
            sql = """
                UPDATE users
                SET {}='{}'
                WHERE {}='{}' AND {}='{}';""".format(setColumn, newValue, whereColumn1, recognizeValue, whereColumn2, recognizeValue2)


 
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
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

        from dataDAO import dataDAO
        dataDAO.dataDecider(dataDAO, self.name, self.password)


    def getGenderFKValue(self, gender):

        sqlGender = """
        SELECT id FROM gender
        WHERE description = '{}';""".format(gender)

        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sqlGender)
        sqlOutput = cur.fetchall()

        for row in sqlOutput:
            value = row[0]

        cur.close()
        conn.commit()

        return value

    def getNationalityFKValue(self, nationality):
        sqlNationality = """
        SELECT id FROM nationality
        WHERE name = '{}';""".format(nationality)

        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sqlNationality)

        sqlOutput = cur.fetchall()

        for row in sqlOutput:
            value = row[0]

        cur.close()
        conn.commit()

        return value