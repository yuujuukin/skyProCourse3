from app.posts.dao.posts_dao import PostsDAO


class SearchDAO(PostsDAO):
    def __init__(self, pic, content, path):
        super().__init__(path)
        self.pic = pic
        self.content = content

    def load_data(self):
        data = super().load_data()
        return data

    def search_post(self, s):
        post = []
        for item in self.load_data():
            if s.lower() in item.content.lower():
                post.append(item)
        return post

    def __repr__(self):
        return f'{self.pic} \n {self.content}'


