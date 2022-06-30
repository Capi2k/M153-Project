from asyncio.windows_events import NULL
from atexit import register
from config import config
import psycopg2
import time

class registerUserDAO:
    def registerUser(self, name, age, password, gender, preference, nationality):
        rgstrUserDAO = registerUserDAO()

        sqlGender = self.createGenderSql(self, gender)

        sqlGenderPreference = self.createGenderSql(self, preference)

        sqlNationality = self.createNationSql(self, nationality)
        
        sql = """
            INSERT INTO users (name, age, password, genderId, preferenceId, nationalityId)
            VALUES ('{}', {}, {}, {}, {}, {})""".format(name, age, password, sqlGender, sqlGenderPreference, sqlNationality)

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
                print('User registered.')
                time.sleep(1)

                # CREATE TABLE users (
                # id              SERIAL PRIMARY KEY,
                # name            VARCHAR(255),
                # age             INTEGER,
                # password        VARCHAR(255),
                # genderId        INTEGER,
                # preferenceId    INTEGER,
                # nationalityId   INTEGER,
                # CONSTRAINT gender_fk FOREIGN KEY (genderId) REFERENCES gender (id),
                # CONSTRAINT preference_fk FOREIGN KEY (preferenceId) REFERENCES gender (id),
                # CONSTRAINT nationality_fk FOREIGN KEY (nationalityId) REFERENCES nationality (id)
                # ); 
    
    def createGenderSql(self, gender):

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

    def createNationSql(self, nationality):
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
