from asyncio.windows_events import NULL
import time
from dataDAO import dataDAO

class menuDAO():

    def menuOptions(self):
        time.sleep(1)
        print('\n')
        print('||| Main-menu |||')
        print('What would you like to do?')
        print('c    Change Data')
        print('s    Swipe')
        print('l    LOGOUT')

        toDo = input()

        if toDo == "l":
            import startDAO
            startDAO
        elif toDo == "c":
            dataDAO.dataDecider(dataDAO)
