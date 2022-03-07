import hashlib
from random import randbytes
# import string
# import secrets

Number_of_rounds = int(input("Введите число раундов: "))

def passw_gen(key, R):
    passw_list = []
    sum = key.encode() + R
    for j in range(Number_of_rounds):
        # password = ''.join(secrets.choice(self.passwd) for i in range(16))
        sum = hashlib.sha1(sum).digest()
        passw_list.append(sum)
        print(sum)
    return passw_list

class Server:

    def __init__(self):
        self.key_base = {}

    def registration(self, log, key):
        # log_info = {log, passwd}
        if log not in self.key_base:
            R = randbytes(16)
            print("Server: данной пары нет в базе ключей. необходима регистрация.")
            I = 1
            # passw = passwd.encode()
            # passwrd = hashlib.sha1(passw).hexdigest()
            passw_gen_1 = passw_gen(key, R)
            self.key_base[log] = [I, passw_gen_1, passw_gen_1[-1]]
            # print("Server: пароль получен", "\n", "Хэшированный пароль: ", passwd)
            print("Server: Вы зарегестрированы. Ваша пара логин-пароль:", self.key_base)
            print("Server: Данные для входа: ", self.key_base)
            # if len(self.key_base) != 0:
            #     print("FULL")
            # else:
            #     print("NULL")
            return R
        else:
            print("Server: Данная пара существует.")
            return None

    def I(self, log):
        return self.key_base[log][0]

    def autentication(self, log, passw):
        # password = passw.encode()
        # passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passw}
        if passw != self.key_base[log][2]:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        else:
            self.key_base[log][0] += 1
            self.key_base[log][2] = self.key_base[log][1][Number_of_rounds - self.key_base[log][0]] #обновление пароля
            print("Число транзакций I увеличено на 1.")
            print("Server: Данная пара существует. Аутентификация прошла успешно. Осуществляется вход.")
            return True
Server = Server()

class User():
    def __init__(self, log, key):
        self.log = log
        self.key = key
        self.passw = []

    def sign_up(self, Server):
        R = Server.registration(self.log, self.key)
        if R is None:
            print("Регистрация не удалась.")
        else:
            self.passw = passw_gen(self.key, R)
            print("Server: Регистрация прошла успешно.")
        # else:
        #     print("Server: Регистрация не удалась.")

    def log_in(self, Server):
        if Number_of_rounds is None:
            print("Server: Аутентификация не удалась.")

        if Server.autentication(self.log, self.passw[Number_of_rounds - Server.I(self.log)]):
            print("Аутентификация прошла успешно")
            return True
        else:
            print("Server: Аутентификация не удалась.")
            return False

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.sign_up(Server)
take.log_in(Server)
#
# take1 = User(input("User: Введите логин: "), input("User: Введите пароль: "))
take.log_in(Server)

take1 = User(take.log, 'x/09')
take1.passw = passw_gen(take1.key, b'gjudckjdsbhj')
take1.log_in(Server)
