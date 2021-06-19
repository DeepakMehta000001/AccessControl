class AccessControl:

    def __init__(self):
        self.users = {}
        self.resources = {}
        self.roles = {'admin': {'id': 1, 'actions': [1,2,3]}, 'user': {'id':2, 'actions': [1]}}
        self.actions = {'READ':1,'WRITE':2,'DELETE':3}
        self.current_user = None
        self.current_role = None

    def add_user(self,name,roles):
        self.users[name]= {'roles': [self.roles[role]['id'] for role in roles], 'resources':[]}

    def add_resource(self,name,actions):
        self.resources[name] = {'actions': [self.actions[action] for action in actions], 'available': True}

    def edit_role(self,user,roles):
        self.users[user]['roles']=[self.roles[role]['id'] for role in roles]

    def valid_roles(self,roles):
        for role in roles:
            if role not in self.roles:
                return False
        return True

    def get_role_by_id(self,role_id):
        for role,details in self.roles.items():
            if role_id==details['id']:
                return role

    def show_users(self):
        print('Below are all the users: ')
        for user,_ in self.users.items():
            print(user)

    def select_user(self,user):
        self.current_user = user
        message = user + ' is selected as '
        if len(self.users[self.current_user]['roles'])>1:
            for role_id in self.users[self.current_user]['roles']:
                role = self.get_role_by_id(role_id)
                print('press '+str(role_id)+ ' for logging as '+role)
            input_role_id = int(input('enter role number: '))
            while input_role_id not in self.users[self.current_user]['roles']:
                input_role_id = int(input('Invalid role number, re-enter role number: '))
            self.current_role = input_role_id
        else:
            self.current_role =  self.users[self.current_user]['roles'][0]
        message += self.get_role_by_id(self.current_role)
        print(message)

    def access_resources(self):
        read_only_resources = []
        real_write_delete_resources = []
        for resource,details in self.resources.items():
            if details['available']:
                if self.actions['WRITE'] in details['actions'] or self.actions['DELETE'] in details['actions'] :
                    real_write_delete_resources.append(resource)
                else:
                    read_only_resources.append(resource)
        if self.roles['admin']['id'] in self.users[self.current_user]['roles']:
            resources = real_write_delete_resources
        elif self.roles['user']['id'] in self.users[self.current_user]['roles']:
            resources = read_only_resources

        if len(resources)==0:
            print('No resources available')
            return None

        print('Below are the list of available resources: ')
        for resource in resources:
            print(resource)
        input_resource = input('Enter the resource to be accessed: ')
        while input_resource not in resources:
            input_resource = input('Invalid resource! Re-enter the resource to be accessed: ')
        self.users[self.current_user]['resources'].append(resource)
        print(resource + ' added to user '+self.current_user+' successfully!')

    def show_options(self):
        # show admin options
        if self.roles['admin']['id'] == self.current_role:
            print('press 1 for login as another user\npress 2 for create user\npress 3 for edit role')
            option = int(input())

            # Login as another user
            if option==1:
                self.show_users()
                selected_user = input('Enter the user name:')
                self.select_user(selected_user)

            # creating a user
            elif option==2:
                user_name = input('Enter user name: ')
                for role,details in self.roles.items():
                     print(str(details['id'])+' for '+role+' role')
                roles = list(map(str, input('Enter role(s) for the user '+ user_name+' in format.. admin or admin,user : ').split(',')))
                while not self.valid_roles(roles):
                    roles = list(map(str, input('Invalid Role! Re-enter role(s) for the user '+ user_name+' in format.. admin or admin,user : ').split(',')))
                self.add_user(user_name,roles)

            # Edit role of a user
            elif option==3:
                self.show_users()
                user_name = input('Enter user name from the list: ')
                while user_name not in self.users:
                    user_name = input('Invalid user name, please retry')
                print('below is the list of roles: ')
                for role,details in self.roles.items():
                     print(str(details['id'])+'.'+role)
                roles = list(map(str, input('Enter role(s) for the user '+ user_name+' in format.. admin or admin,user : ').split(',')))
                while not self.valid_roles(roles):
                    roles = list(map(str, input('Invalid Role! Re-enter role(s) for the user '+ user_name+' in format.. admin or admin,user : ').split(',')))
                self.edit_role(user_name,roles)
            return 'admin_options'
        # show user's options
        elif self.roles['user']['id']  == self.current_role:
            print('press 1 for login as another user\npress 2 for view roles\npress 3 for access resource')
            option = int(input())

            # log in as another user
            if option==1:
                self.show_users()
                selected_user = input('Enter the user name:')
                self.select_user(selected_user)

            # get roles of the user
            elif option==2:
                roles = []
                for role_id in self.users[self.current_user]['roles']:
                    roles.append(self.get_role_by_id(role_id))
                print('role(s) for the user: ', self.current_user, ','.join(roles))

            # access resources
            elif option==3:
                self.access_resources()
            return 'user_options'
