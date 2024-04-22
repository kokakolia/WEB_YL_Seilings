from flask import Flask, render_template, redirect, request
from werkzeug.security import generate_password_hash
import datetime
from loginform import LoginForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/userdata.db')
    app.run(port=5500, host='127.0.0.1')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/main')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = User()
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.sex = request.form['sex']
        user.b_day_date = datetime.datetime.strptime(request.form['b_day'], '%Y-%m-%d').date()
        user.email = request.form['email']
        user.password_hash = generate_password_hash(request.form['password'])
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return 'Ok'

if __name__ == '__main__':
    main()
