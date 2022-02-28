import hashlib

class Server():
    def __init__(self):
        self.key_base = {}
    def registration(self, log, passwd):
        password = passwd.encode()
        passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passwd}
        if log not in self.key_base:
            print("Server: Необходима регистрация.")
            self.key_base[log] = passw
            print("Server: Пароль получен.", "\n", "Хэшированный пароль: ", passw)
            print("Server: Вы зарегестрированы. Ваша пара логин-пароль:", self.key_base)
            print("Server: Данные для входа: ", self.key_base)
            # if len(self.key_base) != 0:
            #     print("FULL")
            # else:
            #     print("NULL")
            return True
        else:
            print("Server: Данная пара существует.")
            return False

    def authentication(self, log, passwd):
        password = passwd.encode()
        passw = hashlib.sha1(password).hexdigest()
        if log not in self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        if passw == self.key_base[log]:
            print("Server: Данная пара существует. Осуществляется вход.")
            return True
        else:
            print("Пароль введён не верно.")
            return False

Server = Server()

class User():
    def __init__(self, log, passwd):
        self.log = log
        self.passwd = passwd
    def log_in(self, Server):
        if Server.authentication(self.log, self.passwd):
            print("Server: Аутентификация прошла успешно.")
        else:
            print("Server: Аутентификация не удалась.")
    def sign_up(self, Server):
        if Server.registration(self.log, self.passwd):
            print("Server: Регистрация прошла успешно.")
        else:
            print("Server: Регистрация не удалась.")

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.sign_up(Server)
take.log_in(Server)

take1 = User(input("User: Введите логин: "), input("User: Введите пароль: "))
take1.log_in(Server)



import hashlib
from random import randbytes

class Server():

    def N_byte(self, log):
        if log in self.key_base.keys():
            N = randbytes(64)
            print(N)
            # self.key_base[log].append(N)
            # self.key_base[log][1] = N
            self.key_base[log][1] = N
            return N

    def __init__(self):
        self.key_base = {}

    def registration(self, log, passw):
        # password = passwd.encode()
        # passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passw}
        if log not in self.key_base:
            self.key_base[log] = {}
            print("Server: данной пары нет в базе ключей. Необходима регистрация.")
            self.key_base[log] = passw
            print("Server: пароль получен", "\n", "Хэшированный пароль: ", passw)
            print("Server: Вы зарегестрированы. Ваша пара логин-пароль:", self.key_base)
            print("Server: Данные для входа: ", self.key_base)
            # if len(self.key_base) != 0:
            #     print("FULL")
            # else:
            #     print("NULL")
            return True
        else:
            print("Server: Данная пара существует.")
            return False

    def authentication(self, log, passw):

        if log not in self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        N = self.key_base[log][1]
        self.key_base[log][1] = 0
        if N == 0:
            return False
        if passw != self.key_base[log]:
            print("Server: Пароль введён не верно.")
            return False
        else:
            print("Пароль введён верно.")
            return True
Server = Server()

class User():
    def __init__(self, log, passw):
        self.log = log
        self.passw = passw
        self.N = 0
    def log_in(self, Server):
        password = self.passw.encode()
        N = Server.N_byte(self.log)
        self.passwrd = hashlib.sha1(password + N).hexdigest()
        if Server.authentication(self.log, self.passwrd):
            print("Аутентификация прошла успешно.")
        else:
            print("Аутентификация не удалась. Повторите попытку позже")

    def sign_up(self, Server):
        if Server.registration(self.log, self.passw):
            print("Server: Регистрация прошла успешно.")
        else:
            print("Server: Регистрация не удалась.")

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.sign_up(Server)
take.log_in(Server)

take1 = User(input("User: Введите логин: "), input("User: Введите пароль: "))
take1.log_in(Server)



import hashlib
from random import randbytes

class Server():

    def N_2_byte(self, log):
        N_2 = randbytes(16)
        print("Server: Сгенерированное сервером значение N_2: ", N_2)
        self.key_base[log][1] = N_2
        return N_2

    def __init__(self):
        self.key_base = {}

    def registration(self, log, passwd):
        password = passwd.encode()
        passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passwd}
        if log not in self.key_base:
            print("Server: данной пары нет в базе ключей. Необходима регистрация.")
            self.key_base[log] = passw
            print("Server: пароль получен", "\n", "Хэшированный пароль: ", passw)
            print("Server: Вы зарегестрированы. Ваша пара логин-пароль:", self.key_base)
            print("Server: Данные для входа: ", self.key_base)
            # if len(self.key_base) != 0:
            #     print("FULL")
            # else:
            #     print("NULL")
            return True
        else:
            print("Server: Данная пара существует.")
            return False

    def authentication(self, log, passwd):
        N_2 = self.key_base[log][1]
        password = passwd.encode()
        passw = hashlib.sha1(password + N_2).hexdigest()
        if log not in self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        if passw != User.passwrd:
            print("Пароль введён не верно.")
            return False
        if passw == self.key_base[log]:
            User_passwd = hashlib.sha1(passw + N_2).hexdigest()
            print("Server: Данная пара существует. Осуществляется вход.")
            return True
        else:
            print("Пароль введён не верно.")
            return False

Server = Server()

class User():

    def N_1_byte(self, log):
        N_1 = randbytes(16)
        print("User: Сгенерированное пользователем значение N_1: ", N_1)
        self.key_base[log][1] = N_1
        return N_1

    def __init__(self, log, passw):
        self.log = log
        self.passw = passw

    def log_in(self, Server):
        password = self.passw.encode()
        N_2 = Server.N_2_byte(self.log)
        passwrd = hashlib.sha1(password + N_2).hexdigest()
        if Server.authentication(self.log, self.passwrd):
            print("Server: Аутентификация прошла успешно.")
        else:
            print("Server: Аутентификация не удалась.")

    def sign_up(self, Server):
        if Server.registration(self.log, self.passw):
            print("Server: Регистрация прошла успешно.")
        else:
            print("Server: Регистрация не удалась.")

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.log_in(Server)
take.sign_up(Server)


import hashlib
from random import randbytes
import string
import secrets

Number_of_rounds = int(input("Введите число раундов: "))
# key = passwd

def passw_gen(self):

    for j in range(Number_of_rounds):
        password = ''.join(secrets.choice(self.passwd) for i in range(16))
        passwrd = self.password.encode()
        passwd_base = hashlib.sha1(passwrd).hexdigest()
        print(passwd_base)
    return passwd_base

class Server:
    I = int(input("Server: Номер транзакции I, переданный сервером: "))

    def __init__(self):
        self.key_base = {}

    def registration(self, log, passwd):
        # log_info = {log, passwd}
        if log not in self.key_base:
            print("Server: данной пары нет в базе ключей. необходима регистрация.")
            I = Number_of_rounds + 1
            # passw = passwd.encode()
            # passwrd = hashlib.sha1(passw).hexdigest()
            self.key_base[log] = self.passw_gen
            print("Server: пароль получен", "\n", "Хэшированный пароль: ", passwd)
            print("Server: Вы зарегестрированы. Ваша пара логин-пароль:", self.key_base)
            print("Server: Данные для входа: ", self.key_base)
            # if len(self.key_base) != 0:
            #     print("FULL")
            # else:
            #     print("NULL")
            return True
        else:
            print("Server: Данная пара существует.")
            return False

    def autentication(self, log, passwd):
        password = passwd.encode()
        passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passw}
        if log != self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        else:
            Server.I += 1
            print("Число транзакций I увеличено на 1.")
            print("Server: Данная пара существует. Аутентификация прошла успешно. Осуществляется вход.")
            return True
Server = Server()

class User():
    def __init__(self, log, passwd):
        self.log = log
        self.passwd = passwd

    def sign_up(self, Server):
        if Server.registration(self.log, self.passwd):
            print("Server: Регистрация прошла успешно.")
        else:
            print("Server: Регистрация не удалась.")

    def log_in(self, Server):
        print("User: Значение I, пришедшее с сервера: ", Server.I)
        if Server.I:
            print("Server: Аутентификация прошла успешно.")
        else:
            print("Server: Аутентификация не удалась.")

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.sign_up(Server)
take.log_in(Server)

take1 = User(input("User: Введите логин: "), input("User: Введите пароль: "))
take1.log_in(Server)
