from asyncio.windows_events import NULL
#import psycopg2
import time
from config import config
from os import system
from menuDAO import menuDAO

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