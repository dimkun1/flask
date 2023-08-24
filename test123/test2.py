from pathlib import PurePath, Path
from flask import Flask, render_template, request, abort, url_for, redirect, flash, make_response, session
from werkzeug.utils import secure_filename
from markupsafe import escape
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()



@app.route('/')
def main():
    return render_template('main.html')


@app.route('/hello/')
def hello1():
    return 'привет мир'





@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == "POST":
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static/img', file_name))
        return render_template('task2_1.html', file_name=file_name)
    return render_template('task_2.html')







users = {"admin": '12345', "guest": '00000'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if (username, password) in users.items():
            return "успешно"
        return f"неверно логи {escape(username)} или пароль {escape(password)}"
    return render_template("task_3.html")



@app.route('/count', methods=['GET', 'POST'])
def count():
    if request.method == "POST":
        text = request.form.get('text')
        return f"кол во введенных слов {len(text.split())}"
    return render_template("task_4.html")



@app.route('/culc/', methods=['GET', 'POST'])
def culc():
    if request.method == "POST":
        number1 = int(request.form.get("number1"))
        number2 = int(request.form.get("number2"))
        operation = request.form.get("operation")
        if operation == 'add':
            return f"{number1 + number2}"
        elif operation == 'subtract':
            return f"{number1 - number2}"
        elif operation == 'mulpiply':
            return f"{number1 * number2}"
        elif operation == 'divide':
            return f"{number1 / number2}"
    return render_template('task_5.html')


@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if age < 18:
            return abort(403)
        return f"{name}, есть 18"
    return render_template('task_6.html')


@app.errorhandler(403)
def age_age_not(e):
    print(e)
    return render_template('403.html'), 403

@app.route('/num_num/', methods=['GET', 'POST'])
def num_num():
    if request.method == "POST":
        number = int(request.form.get("number"))
        result = number**2
        return redirect(url_for('num_result', result=result))
    return render_template('task_7.html')

@app.route('/num_result/')
def num_result():
    return request.args.get('result')



@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        name = request.form.get('name')
        flash(f'Hello {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('task_8.html')










@app.route('/index1/', methods=['GET', 'POST'])
def index1():
    return render_template('task_9.html')

@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect('/great'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response

@app.route('/great/', methods=['GET', 'POST'])
def great():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('great.html', name=user_name)
    return render_template('/index1/')

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    response = make_response(redirect('/index1/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response









@app.route('/index2/', methods=['GET', 'POST'])
def index2():
    return render_template('task_10.html')

@app.route('/login2/', methods=['GET', 'POST'])
def login2():
    if request.method == "POST":
        session['username'] = request.form.get('username', 'email')
        return redirect(url_for('task_10.html'))
    return render_template('great2.html')

@app.route('/logout2/', methods=['GET', 'POST'])
def logout2():
    session.pop('username', None)
    return redirect(url_for('task_10.html'))








if __name__ == '__main__':
    app.run(debug=True)
