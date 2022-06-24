from asyncio.windows_events import NULL
#import psycopg2
import time
from config import config
from os import system
from loginDAO import loginDAO
#from start import startDAO

class registerDAO():

    countries = ["CH", "DE", "FR", "AU", "SP", "NL", "IT", "ES", "SE", "BE", "LU", "DK", "NO", "FI", "PL", "PT", "CZ", "GB", "IE"]

    def inputName(self):
        time.sleep(1)
        print('Enter your firstname (Or e to EXIT)')
        name = input()
        if name == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            time.sleep(1)
            self.inputAge(self)

    def inputAge(self):
        print('Enter your age (Or e to EXIT)')
        age = input()
        if age == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            time.sleep(1)
            self.inputPassword(self)

    def inputPassword(self):
        print('Enter your password (Or e to EXIT)')
        password = input()
        if password == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            time.sleep(1)
            self.inputGender(self)

    def inputGender(self):
        print('Enter your gender (M=male, F=female, E=else) (Or e to EXIT)')
        gender = input()
        if gender == "M" or gender == "F" or gender == "E":
            time.sleep(1)
            self.inputPreference(self)
        elif gender == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            print('invalid input')
            time.sleep(1)

    def inputPreference(self):
        print('Enter your gender preference (M=male, F=female, E=else) (Or e to EXIT)')
        genderPreference = input()
        if genderPreference == 'M' or genderPreference == 'F' or genderPreference == "E":
            time.sleep(1)
            self.inputNationality(self)
        elif genderPreference == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            print('invalid input')
            time.sleep(1)
            self.inputPreference(self)

    def inputNationality(self):
        print('And as a last step, please enter your nationality (Country like CH, DE, AU, FR etc) (Or e to EXIT)')
        nationality = input()
        if nationality in self.countries:
            print('Perfect, we got all the information we need')
            print('We will now guide you to the login page')
            loginDAO.login(loginDAO)
            time.sleep(1)
        elif nationality == "e":
            print("Going back to main-menu")
            time.sleep(1)
        else:
            print('invalid input')
            time.sleep(1)
            self.inputNationality(self)
