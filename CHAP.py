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
        return None

    def __init__(self):
        self.key_base = {}

    def registration(self, log, passw):
        password = passw.encode()
        passw = hashlib.sha1(password).hexdigest()
        # log_info = {log, passw}
        if log not in self.key_base:
            print("Server: данной пары нет в базе ключей. Необходима регистрация.")
            self.key_base[log] = [passw.encode(), None]
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

    def authentication(self, log, hash_passw):

        if log not in self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        N = self.key_base[log][1]
        self.key_base[log][1] = None
        string = N + self.key_base[log][0]
        hash_key = hashlib.sha1(string).hexdigest()
        if N is None:
            return False
        if hash_passw != hash_key:
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
    def log_in(self, Server):
        N = Server.N_byte(self.log)
        if N is None:
            print("Аутентификация не удалась.")
            return False
        password = self.passw.encode()
        passwrd = hashlib.sha1(password).hexdigest()
        string = N + passwrd.encode()
        hash_passw = hashlib.sha1(string).hexdigest()

        if Server.authentication(self.log, hash_passw):
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
