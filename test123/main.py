from flask import Flask
from flask import render_template

app = Flask(__name__)



#
# @app.route('/<int:num_a>/<int:num_b>/')
# def fun(num_a, num_b):
#     return f'{num_a} + {num_b} = {num_a + num_b}'
#
#
# @app.route('/<text>/')
# def len_text(text):
#     return f'длина строки {text} - {len(text)} символов'
#
#
# html = """
# <h1>Привет, меня зовут Алексей</h1>
# <p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
# """
#
#
# @app.route('/hello/')
# def hello():
#     return html
#
#
# students = [
#     {"firstname": "alex", "lastname": "berta", "age": 26, "rate": 2},
#     {"firstname": "fred", "lastname": "berol", "age": 24, "rate": 3},
#     {"firstname": "ben", "lastname": "beeu", "age": 18, "rate": 4}
# ]
#
#
# @app.route('/students/')
# def get_students():
#     return render_template("students.html", students=students)
#
#
# class News:
#     def __init__(self, title, descriptions, date):
#         self.title = title
#         self.descriptions = descriptions
#         self.date = date
#
#
# @app.route('/news/')
# def news():
#     news = [News("какая то новость", "описание", "дата"), News("какая то новость", "описание", "дата"),
#             News("какая то новость", "описание", "дата"), News("какая то новость", "описание", "дата"),
#             News("какая то новость", "описание", "дата"), News("какая то новость", "описание", "дата")]
#     return render_template("news.html", news=news)


@app.route('/')
def start():
    return render_template('base.html', title="домашняя страница")


@app.route('/about/')
def about():
    return render_template('about.html', title="о нас")


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', title="контакты")

@app.route('/magazin/')
def magazin():
    return render_template('magazin.html', title="Магазин")

@app.route('/magazin/obuv/')
def magazin_obuv():
    return render_template('obuv.html', title="обувь")

@app.route('/magazin/odejda/')
def magazin_odejda():
    return render_template('odejda.html', title="одежда")





if __name__ == '__main__':
    app.run(port=5001, debug=True)
