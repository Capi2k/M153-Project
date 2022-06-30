from asyncio.windows_events import NULL
from optparse import Values
#import psycopg2
import time
from config import config
from os import system
from menuDAO import menuDAO

# compare input values with database Values
# https://stackoverflow.com/questions/57636773/how-to-compare-input-value-with-mysql-database-value-in-python
# https://stackoverflow.com/questions/69300218/how-can-i-compare-a-value-from-database-to-python-input


class loginDAO():

    def login(self):
        print('Since there is no database usage yet, you are automatically "logged in" (lol, sure)')
        time.sleep(1)
        menuDAO.menuOptions(menuDAO)

    def actualLogin(self):
        print('\n')
        print('||| Login |||')
        self.enterName(self)

    def enterName(self):
        print('Enter your name')
        name = input()
        self.enterPassword(self)

    def enterPassword(self):
        print('Enter your password')
        password = input()