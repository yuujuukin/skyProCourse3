from flask import Blueprint, render_template
from .dao.users_dao import UsersDAO

users_blueprint = Blueprint('users_blueprint', __name__, template_folder="templates")
users_dao = UsersDAO('./data/posts.json')


@users_blueprint.route('/users/')
def page_all_users():
    users = users_dao.get_all()
    return render_template('users_index.html', users=users)


@users_blueprint.route('/users/<string:poster_name>/')
def page_single_user(poster_name):
    user = users_dao.load_single_user(poster_name)
    return render_template('users_single.html', user=user)

