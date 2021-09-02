import os

def title():
    print('**************************************')
    print('*   Welcome to XAMPP Control Panel   *')
    print('*      Developed by Billy Kwek       *')
    print('**************************************\n')

def clear():
    os.system('clear')

def main():
    clear()
    title()

    print('What you do you wanna do?\n')
    print(' 1. Start XAMPP')
    print(' 2. Stop XAMPP')
    print(' 3. Restart XAMPP')
    print(' 4. Hit any of those motherfucking key to EXIT\n')

    user = int(input('Choose: '))

    if user == 1:
        os.system('sudo /opt/lampp/lampp start')
    elif user == 2:
        os.system('sudo /opt/lampp/lampp stop')
    elif user == 3:
        os.system('sudo /opt/lampp/lampp restart')
    else:
        pass

if __name__ == '__main__':
    main()
