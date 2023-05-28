import json


class Post:
    def __init__(self, pic, content, poster_name):
        self.pic = pic
        self.content = content
        self.poster_name = poster_name


# класс постов
class PostsDAO:

    # настраиваем функцию для пути
    def __init__(self, path):
        self.path = path

    # читаем файл
    def load_data(self):
        posts = []

        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            poster_name = item["poster_name"]
            content = item["content"]
            pic = item.get('pic')
            post = Post(pic, content, poster_name)
            posts.append(post)
        return posts

    # загружаем все посты
    def get_all(self):
        posts = self.load_data()
        return posts

    # вывод поста по pk
    def get_by_pk(self, pk):
        posts = self.load_data()
        for post in posts:
            if post["pk"] == pk:
                return post

    # поиск поста по ключевому слову
    def search_post(self, query, posts: list[Post]) -> list[Post]:
        result = []
        for post in posts:
            if query in post.content:
                result.append(post)
        return result

