from asyncio.windows_events import NULL
import time
from swipeUserDAO import swipeUserDAO

class swipeDAO():

    name = ''
    password = ''

    def swipeProcess(self, name, password):
        swipeUserDAO.findPotentialMatches(swipeUserDAO, name, password)
        self.name = name
        self.password = password

    
        
