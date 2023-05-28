import posts as posts
from flask import Blueprint, render_template, request
from .dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")
posts_dao = PostsDAO("./data/posts.json")


@posts_blueprint.route('/posts/')
def page_all_posts():
    posts = posts_dao.get_all()
    return render_template("posts_index.html", posts=posts)


@posts_blueprint.route('/posts/<int:pk>/')
def page_pk_posts(pk):
    post = posts_dao.get_by_pk(pk)
    return render_template("posts_single.html", post=post)


@posts_blueprint.route('/post_list')
def search():
    s = request.args.get('s', '') # использовать get для получения значения параметра s
    dao = PostsDAO('data/posts.json')
    all_posts = dao.load_data()
    # Отфильтровываем посты, содержащие заданное ключевое слово
    filtered_posts = [post for post in all_posts if s in post.content]
    # Передаём отфильтрованные посты в шаблон
    return render_template('post_list.html', posts=filtered_posts)
