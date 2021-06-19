
def create_data(access_control):
    print('adding an admin user')
    access_control.add_user('deepak',['admin'])
    print('adding a normal user')
    access_control.add_user('arun',['user'])
    print('adding two read only resources')
    access_control.add_resource('R1', ['READ'])
    access_control.add_resource('R2', ['READ'])
    print('adding two read,write resources')
    access_control.add_resource('R3', ['READ','WRITE'])
    access_control.add_resource('R4', ['READ','WRITE'])
    print('adding one read,delete resource')
    access_control.add_resource('R5', ['READ','DELETE'])
