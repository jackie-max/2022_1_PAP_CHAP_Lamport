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
