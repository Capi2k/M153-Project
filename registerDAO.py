from asyncio.windows_events import NULL
#import psycopg2
import time
from config import config
from os import system
from loginDAO import loginDAO
from registerUserDAO import registerUserDAO
#from start import startDAO

class registerDAO():

    countries = ["CH", "DE", "FR", "AU", "SP", "NL", "IT", "ES", "SE", "BE", "LU", "DK", "NO", "FI", "PL", "PT", "CZ", "GB", "IE"]

    name = ''
    age = ''
    password = ''
    gender = ''
    genderPreference = ''
    nationality = ''


    def inputName(self):
        time.sleep(1)
        print('Enter your firstname (Or e to EXIT)')
        self.name = input()
        if self.name == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            self.inputAge(self)

    def inputAge(self):
        print('Enter your age (Or e to EXIT)')
        self.age = input()
        if self.age == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            self.inputPassword(self)

    def inputPassword(self):
        print('Enter your password (Or e to EXIT)')
        self.password = input()
        if self.password == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            self.inputGender(self)

    def inputGender(self):
        print('Enter your gender (M=male, F=female, E=else) (Or e to EXIT)')
        self.gender = input()
        if self.gender == "M" or self.gender == "F" or self.gender == "E":
            time.sleep(0.5)
            self.inputPreference(self)
        elif self.gender == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            print('invalid input')
            time.sleep(0.5)
            self.inputGender(self)

    def inputPreference(self):
        print('Enter your gender preference (M=male, F=female, E=else) (Or e to EXIT)')
        self.genderPreference = input()
        if self.genderPreference == 'M' or self.genderPreference == 'F' or self.genderPreference == "E":
            time.sleep(0.5)
            self.inputNationality(self)
        elif self.genderPreference == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            print('invalid input')
            time.sleep(0.5)
            self.inputPreference(self)

    def inputNationality(self):
        print('And as a last step, please enter your nationality (Country like CH, DE, AU, FR etc) (Or e to EXIT)')
        self.nationality = input()
        if self.nationality in self.countries:
            print('Perfect, we got all the information we need')
            print('We will now guide you to the login page')
            registerUserDAO.registerUser(registerUserDAO, self.name, self.age, self.password, self.gender, self.genderPreference, self.nationality)
            loginDAO.login(loginDAO)
            time.sleep(0.5)
        elif self.nationality == "e":
            print("Going back to main-menu")
            time.sleep(0.5)
        else:
            print('invalid input')
            time.sleep(0.5)
            self.inputNationality(self)
