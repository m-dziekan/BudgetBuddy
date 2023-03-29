from modules.login import Login
from modules.home_window import HomeWindow
import os
from modules.database.database_connect import DatabaseConnector


def main():
    try:
        with open('login_pass.txt') as f:
            lines = f.readlines()

        user_login = lines[0].strip('\n')
        user_pass = lines[1]
        db = DatabaseConnector()

        login_query = f"SELECT username, password FROM users WHERE username = '{user_login}' " \
                      f"AND password = crypt('{user_pass}', password);"
        credentials = db.select_data(login_query, 'one')

        if credentials is not None:
            home_window = HomeWindow(user_login)
            home_window.mainloop()
        else:
            login_screen = Login()
            login_screen.mainloop()
    except IOError:
        login_screen = Login()
        login_screen.mainloop()


if __name__ == '__main__':
    main()
