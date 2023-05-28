import json


# класс пользователей
class UsersDAO:

    def __init__(self, path):
        self.path = path

    # загружаем всё из json файла
    def load_all_users(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    # загржаем всех пользователей
    def get_all(self):
        users = self.load_all_users()
        return users

    # поиск по имени
    def load_single_user(self, poster_name):
        users = self.load_all_users()
        for user in users:
            if user["poster_name"] == poster_name:
                return user
