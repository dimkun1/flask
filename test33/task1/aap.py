from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from flask import Flask, render_template, jsonify, request
from test33.task1.models import db, User, Post
import secrets
from flask_wtf.csrf import CSRFProtect
from test33.task1.forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../instance/mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'hi'

@app.route('/data/')
def data():
    return 'you data'


#
# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#     print("ok")
#
#
# @app.cli.command('add-john')
# def add_user():
#     user = User(username='John', email='john@example.com')
#     db.session.add(user)
#     db.session.commit()
#     print("John in add db")
#
# @app.cli.command('edit-john')
# def edit_user():
#     user = User.query.filter_by(username='John').first()
#     user.email = 'new_email@examples.com'
#     db.session.commit()
#     print("edit John in add db")
#
# @app.cli.command('del-john')
# def del_user():
#     user = User.query.filter_by(username='John').first()
#     db.session.delete(user)
#     db.session.commit()
#     print("delete John in add db")
#
#
# @app.cli.command("fill-db")
# def fill_tables():
#     count = 5
#     # Добавляем пользователей
#     for user in range(1, count + 1):
#         new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
#         db.session.add(new_user)
#     db.session.commit()
#
#
#     # Добавляем статьи
#     for post in range(1, count ** 2):
#         author = User.query.filter_by(username=f'user{post % count + 1}').first()
#         new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
#         db.session.add(new_post)
#     db.session.commit()

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
