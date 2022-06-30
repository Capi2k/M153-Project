from asyncio.windows_events import NULL
import time
from dataDAO import dataDAO
from swipeDAO import swipeDAO

class menuDAO():

    name = ''
    password = ''

    def menuOptions(self, name, password):

        self.name = name
        self.password = password

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
        elif toDo == "s":
            swipeDAO.swipeProcess(swipeDAO, self.name, self.password)
        elif toDo == "c":
            dataDAO.dataDecider(dataDAO, self.name, self.password)
