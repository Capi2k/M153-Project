from asyncio.windows_events import NULL
import time
from updateDataDAO import updateDataDAO

class dataDAO():

    def dataDecider(self):
        time.sleep(1)
        print('\n')
        print('||| Which of your data do you want to change? |||')
        print('n    Name')
        print('p    Password')
        print('a    Age')
        print('g    Gender')
        print('gp   Gender preference')
        print('b    BACK')

        change = input()
        if change == "b":
            time.sleep(1)
            print('Returning to the Main-menu')
            time.sleep(1)
            import menuDAO
            menuDAO.menuOptions(menuDAO)
        elif change == "n":
            self.changeName(self)
        elif change == "p":
            self.changePassword(self)
        elif change == "a":
            self.changeAge(self)
        elif change == "g":
            self.changeGender(self)
        elif change == "gp":
            self.changeGenderPreference(self)
        else:
            print('invalid input')
    
    def changeName(self):
        time.sleep(1)
        print('Enter your new name (e to exit)')
        name = input()
        if name == "e":
            self.dataDecider(self)
        else:
            #TODO: change Name in DB according to userID
            updateDataDAO.updateData(updateDataDAO, 'name', name,)
            print('')

    def changePassword(self):
        time.sleep(1)
        print('Enter your new password (e to exit)')
        password = input()
        if password == "e":
            self.dataDecider(self)
        else:
            #TODO: change Password in DB
            print('')

    def changeAge(self):
        time.sleep(1)
        print('Enter your new age (e to exit)')
        age = input()
        if age == "e":
            self.dataDecider(self)
        else:
            #TODO: change Age in DB
            print('')

    def changeGender(self):
        time.sleep(1)
        print('Enter your new gender (F,M or E) (e to exit)')
        gender = input()
        if gender == "e":
            self.dataDecider(self)
        else:
            #TODO: change Gender in DB
            print('')

    def changeGenderPreference(self):
        time.sleep(1)
        print('Enter your new gender preference (F,M or E) (e to exit)')
        genderPreference = input()
        if genderPreference == "e":
            self.dataDecider(self)
        else:
            #TODO: change Gender Preference in DB
            print('')
