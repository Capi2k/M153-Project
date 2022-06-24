from asyncio.windows_events import NULL
from registerDAO import registerDAO

class startDAO():

    def navigateToLogin(self):
        print('login')

    def navigateToRegister(self):
        registerDAO.inputName(registerDAO)


def main():
    strtDAO = startDAO()
    toDo = ''
    num = 0
    while toDo != '4':
        print('||| Hello there and welcome to "Love on the first bit" \u2122 |||')
        print('What do you want to do:')
        print('l    Login')
        print('r    Register')
        print('q    QUIT')

        ##dbGUI.printMenu(num)

        toDo = input()
        if toDo == 'l':
            startDAO.navigateToLogin(strtDAO)
        elif toDo == 'r':
            startDAO.navigateToRegister(strtDAO)
        elif toDo == 'q':
            print('👋')
            toDo = '4'
        else:
            print('wrong command')


if __name__ == '__main__':
    main()