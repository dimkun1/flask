from flask import Flask
from test33.task1.models import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'hi'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("ok")



if __name__ == '__main__':
    app.run(debug=True)
