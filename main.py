from data import create_data
from controller import AccessControl

if __name__=='__main__':
    print('adding initial data')
    access_control = AccessControl()
    create_data(access_control)
    print('Running main --- enter ctrl+c to exit')
    access_control.show_users()
    selected_user = input('Enter the user name:')
    access_control.select_user(selected_user)
    while True:
        print('Hi! you are logged in as '+access_control.current_user)
        access_control.show_options()
