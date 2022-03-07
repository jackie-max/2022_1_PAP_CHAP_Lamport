import hashlib
from random import randbytes

class Server():

    def N_2_byte(self, log):
        if log in self.key_base.keys():
            N_2 = randbytes(64)
            print(N_2)
            # self.key_base[log].append(N)
            # self.key_base[log][1] = N
            self.key_base[log][1] = N_2
            return N_2
        return None

    def __init__(self, log, passw):
        self.key_base = {}
        self.log = log
        self.passw = passw

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
            return (self.log, self.passw)
        else:
            print("Server: Данная пара существует.")
            return None

    def authentication(self, log, hash_passw, N_1):
        if log not in self.key_base:
            print("Server: Ошибка: данной пары нет в базе ключей. Проверьте логин и пароль или зарегестрируйтесь.")
            return False
        N_2 = self.key_base[log][1]
        self.key_base[log][1] = None
        string = N_2 + self.key_base[log][0]
        hash_key = hashlib.sha1(string).hexdigest()
        if hash_passw != hash_key:
            print("Server: Пароль введён не верно.")
            return None
        else:
            print("Пароль введён верно.")
            string_1 = N_1 + self.passw.encode()
            hash_string = hashlib.sha1(string_1).hexdigest()
            return (self.log, hash_string)

Server = Server("log", "passw")

class User():

    def N_1_byte(self):
        return randbytes(64)

    def __init__(self, log, passw):
        self.key_base = {}
        self.log = log
        self.passw = passw

    def log_in(self, Server):
        N_1 = self.N_1_byte()
        N_2 = Server.N_2_byte(self.log)
        string = N_2 + hashlib.sha1(self.passw.encode()).hexdigest().encode()
        hash_key = hashlib.sha1(string).hexdigest()
        # if Server.authentication(self.log, hash_key, N_1):
        #     print("Server: Аутентификация прошла успешно.")
        # else:
        #     print("Server: Аутентификация не удалась.")
        response = Server.authentication(self.log, hash_key, N_1)
        if response is None:
            print("Server: Аутентификация не удалась.")
        else:
            log, hash_key_1 = response
            if log not in self.key_base:
                print("Аутентификация не удалась.")
            else:
                hash_new = hashlib.sha1(N_1 + self.key_base[log].encode()).hexdigest()
                if hash_new == hash_key_1:
                    print("Аутентификация прошла успешно.")
                else:
                    print("Аутентификация не удалась.")

    def sign_up(self, Server):
        response = Server.registration(self.log, self.passw)
        if response is None:
            print("Server: Регистрация не удалась.")
        else:
            self.key_base[response[0]] = response[1]
            print("Server: Регистрация прошла успешно.")

take = User(input("User: Введите логин: "), input("User: Введите пароль: "))

take.sign_up(Server)
take.log_in(Server)

take.passw = input("User: Введите пароль: ")
take.log_in(Server)
