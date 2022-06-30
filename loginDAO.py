from asyncio.windows_events import NULL
from optparse import Values
#import psycopg2
import time
from config import config
from os import system
from loginUserDAO import loginUserDAO
# compare input values with database Values
# https://stackoverflow.com/questions/57636773/how-to-compare-input-value-with-mysql-database-value-in-python
# https://stackoverflow.com/questions/69300218/how-can-i-compare-a-value-from-database-to-python-input


class loginDAO():

    username = ''
    password = ''

    def login(self):
        print('\n')
        print('||| Login |||')
        time.sleep(0.5)
        self.enterName(self)

    def enterName(self):
        print('Enter your name')
        time.sleep(0.5)
        self.username = input()
        self.enterPassword(self)

    def enterPassword(self):
        print('Enter your password')
        time.sleep(0.5)
        self.password = input()
        self.checkForUserOnDb(self)

    def checkForUserOnDb(self):
        loginUserDAO.loginUser(loginUserDAO, self.username, self.password)