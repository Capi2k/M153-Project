from asyncio.windows_events import NULL
import time
from updateDataDAO import updateDataDAO

class dataDAO():

    name = ''
    password = ''

    def dataDecider(self, name, password):
        
        self.name = name
        self.password = password

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
            updateDataDAO.updateData(updateDataDAO, 'name', name, 'name', self.name, 'password', self.password)
            print('')

    def changePassword(self):
        time.sleep(1)
        print('Enter your new password (e to exit)')
        password = input()
        if password == "e":
            self.dataDecider(self)
        else:
            #TODO: change Password in DB
            updateDataDAO.updateData(updateDataDAO, 'password', password, 'name', self.name, 'password', self.password)
            print('')

    def changeAge(self):
        time.sleep(1)
        print('Enter your new age (e to exit)')
        age = input()
        if age == "e":
            self.dataDecider(self)
        else:
            updateDataDAO.updateData(updateDataDAO, 'age', age, 'name', self.name, 'password', self.password)
            #TODO: change Age in DB
            print('')

    def changeGender(self):
        time.sleep(1)
        print('Enter your new gender (F,M or E) (e to exit)')
        gender = input()
        if gender == "e":
            self.dataDecider(self)
        else:
            updateDataDAO.updateData(updateDataDAO, 'gender', gender, 'name', self.name, 'password', self.password)
            #TODO: change Gender in DB
            print('')

    def changeGenderPreference(self):
        time.sleep(1)
        print('Enter your new gender preference (F,M or E) (e to exit)')
        preference = input()
        if preference == "e":
            self.dataDecider(self)
        else:
            updateDataDAO.updateData(updateDataDAO, 'preference', preference, 'name', self.name, 'password', self.password)
            #TODO: change Gender Preference in DB
            print('')

    def changeNationality(self):
        time.sleep(1)
        print('Enter your new nationality (Country like CH, DE, AU, FR etc) (e to exit)')
        nationality = input()
        if nationality == "e":
            self.dataDecider(self)
        else:
            updateDataDAO.updateData(updateDataDAO, 'nationality', nationality, 'name', self.name, 'password', self.password)
            #TODO: change Gender Preference in DB
            print('')
