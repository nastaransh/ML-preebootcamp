import re
import hashlib


class Account:

    def __init__(self, user_name, password, phone, Email):
        self.user_name = Account.check_username(user_name)
        self.password = Account.check_password(password)
        self.phone = Account.check_phone(phone)
        self.Email = Account.check_email(Email)

    @staticmethod
    def check_username(user_name):
        user_name = str(user_name)
        chk_u = re.search(r"\b[a-zA-Z]+_+[a-zA-Z]+\b", user_name)
        if chk_u:
            return user_name
        else:
            raise Exception('Invalid username')

    @staticmethod
    def check_password(password):
        chk_p = re.fullmatch('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}', password)
        if chk_p:
            hash_pass =  hashlib.sha256(password.encode('utf-8')).hexdigest()
            return hash_pass
        else:
            raise Exception('Invalid password')

    @staticmethod
    def check_phone(phone):
        chk_ph = re.search(r"^(989|09)\d{9}\b", phone)
        if chk_ph:
            return '09' + phone[-9:]
        else:
            raise Exception('Invalid phone number')

    @staticmethod
    def check_email(Email):
        chk_em = re.fullmatch('[a-zA-Z0-9._-]+@[a-zA-Z0-9]+.[a-zA-z]{2,5}', Email)
        if chk_em:
            return Email
        else:
            raise Exception('Invalid Email')


# us = input('enter us')
# pas = input('enter pass')
# ph = input('enter ph')
# ema = input('enter em')
# user2 = Account('nas_sh', '123456hG', '09124401433', 'nas@gmail.com')

class Site:
    def __init__(self,URL):
        self.URL=URL
        self.register_users = []
        self.active_users  = []

    def register(self,u):
        if u in self.register_users:
            if u.user_name == user.user_name:
                raise Exception ('User already registered')
        else:
            self.register_users.append(u)
            return self.register_users

    def login(self,*args):
        check_p = 0
        for users in self.active_users:

            if len(args) == 3:
                 if users.Email == args[0] and users.user_name == args[1] and users.password == hashlib.sha256(args[1].encode('utf-8')).hexdigest():
                    print('user already logged in')
                    check_p = 1
            elif len(args) == 2:
                if (users.Email == args[0] or users.user_name == args[0]) and users.password == hashlib.sha256(args[1].encode('utf-8')).hexdigest():
                    print('user already logged in')
                    check_p = 1
        if check_p != 1:
            for users in self.register_users:
                if len(args) == 3:
                    if users.Email == args[0] and users.user_name == args[1] and users.password == hashlib.sha256(rgs[2].encode('utf-8')).hexdigest():
                        self.active_users.append(users)
                        print('login successful')
                        check_p = 2
                elif len(args) == 2:
                    if (users.Email == args[0] or users.user_name == args[0]) \
                            and users.password == hashlib.sha256(args[1].encode('utf-8')).hexdigest():
                        self.active_users.append(users)
                        print('login successful')
                        check_p = 2
        if check_p == 0:
            print('invalid login')

    def logout(self,username):
        if username in self.active_users:
            self.active_users.remove(username)
            print('logout successful')
        else:
            print('user is not logged in')

user = Account('sina_abdi', 'Ss123456789', '09124401433', 'sina@gmail.com')
user2 = Account('sina_abdi', 'Ss123456789', '09124401433', 'sina@gmail.com')
site = Site('www')
site.register(user)
site.register(user2)

site.login('sina_abdi', 'Ss123456789')
site.login('sina_abdi', 'Ss123456789')
