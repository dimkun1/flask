from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def start():
    return f'start'


@app.route('/<int:num_a>/<int:num_b>/')
def fun(num_a, num_b):
    return f'{num_a} + {num_b} = {num_a + num_b}'


@app.route('/<text>/')
def len_text(text):
    return f'длина строки {text} - {len(text)} символов'


html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/hello/')
def hello():
    return html


students = [
    {"firstname": "alex", "lastname": "berta", "age": 26, "rate": 2},
    {"firstname": "fred", "lastname": "berol", "age": 24, "rate": 3},
    {"firstname": "ben", "lastname": "beeu", "age": 18, "rate": 4}
]


@app.route('/students/')
def students():
    return render_template("students.html", students=students)


if __name__ == '__main__':
    app.run(debug=True)
