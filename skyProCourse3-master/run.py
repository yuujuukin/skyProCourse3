from flask import Flask, render_template

from app.posts.views import posts_blueprint
from app.users.views import users_blueprint

app = Flask(__name__)


@app.route("/")
def main_page():
	return render_template('index.html')

app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
	app.run()