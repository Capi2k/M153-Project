from asyncio.windows_events import NULL
from atexit import register
from config import config
import psycopg2
import time

class swipeUserDAO:

    id = ''
    name = ''
    password = ''
    userGender = ''
    userPreference = ''
    datingData = ''
    datingDataId = ''


    def findPotentialMatches(self, name, password):
        self.name = name
        self.password = password

        sqlPreference = """
        SELECT id, genderid, preferenceid FROM users
        WHERE name='{}' and password='{}'
        """.format(name, password)



        conn = None
        try:
            # read the connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            # get the users gender and preference
            cur.execute(sqlPreference)

            sqlPreferences = cur.fetchall()

            for row1 in sqlPreferences:
                self.id = row1[0]
                self.userGender = row1[1]
                self.userPreference = row1[2]

            sql = """
            SELECT id, name, age FROM users
            WHERE genderid='{}' and preferenceid='{}';
            """.format(self.userPreference, self.userGender)

            # get all user that match the users gender and preference
            cur.execute(sql)

            sqlOutput = cur.fetchall()

            counter = 0
            self.datingData = [0 for x in range(30)]
            for row in sqlOutput:
                self.datingData[counter] = row[1]
                counter += 1
                self.datingData[counter] = row[2]
                counter += 1

            retnuoc = 0
            self.datingDataId = [0 for x in range(10)]
            for wor in sqlOutput:
                self.datingDataId[retnuoc] = wor[0]
                retnuoc += 1



            # close communication with the PostgreSQL database server
            cur.close()

            # commit the changes
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                self.startSwiping(self, self.datingData, self.datingDataId, self.id)



    def startSwiping(self, datingData, datingDataId, userId):
        counterId = 0
        counter = 0
        
        for x in datingData:
            y = datingDataId[counterId]
            print(x)
            counter += 1
            if(x == 0):
                print('As it seems you have ran out of possible options for people to date.')
                time.sleep(2)
                print('We will now bring you back to the main menu')
                time.sleep(1)
                from menuDAO import menuDAO
                menuDAO.menuOptions(menuDAO, self.name, self.password)
            else:
                if(counter == 2):
                    print('Would  you like to get in touch with this person?')
                    print('y    yes')
                    print('n    no')
                    print('e    exit swiping')
                    answer = input()
                    print('\n')
                    if(answer == "y"):
                        self.createMatch(self, self.id, y)
                        counter = 0
                        counterId += 1
                        continue
                    elif(answer == "n"):
                        print('\n')
                        counter = 0
                        counterId += 1
                        continue
                    elif(answer == "e"):
                        counter = 0
                        counterId += 1
                        print('We will bring you back \n')
                        time.sleep(0.5)
                    else:
                        counter = 0
                        print("Invalid input, woops, they're gone \n")
                        time.sleep(0.5)
                        counterId += 1
                        continue

    def createMatch(self, userId, matchId):
        
        sql = """
            INSERT INTO matches (user1id, user2id)
            VALUES ('{}', '{}')""".format(userId, matchId)

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                time.sleep(1)
    
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

