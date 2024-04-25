from flask import Flask, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message, Mail
from forms import LoginForm, RegisterForm, VerifyForm
from data import db_session
from data.users import User
from bot import bot_send_order
from flask_login import login_user, LoginManager
from random import randint


app = Flask(__name__, template_folder='static/templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_DEFAULT_SENDER'] = 'tlt.ceilings63@gmail.com'
app.config['MAIL_USERNAME'] = 'tlt.ceilings63@gmail.com'
app.config['MAIL_PASSWORD'] = 'yedk uijg enpw zjhg'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail()
mail.init_app(app)
with app.app_context():
    message = Message(subject='Код для подтверждения регистрации')


users_info = {

}


def main():
    db_session.global_init('db/userdata.db')
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def setup_user(data):
    surname = data['surname']
    name = data['name']
    sex = data['sex']
    b_day = data['b_day']
    email = data['email']
    password = data['pwd']
    db_sess = db_session.create_session()
    user = User(
        surname=surname,
        name=name,
        sex=sex,
        b_day_date=b_day,
        email=email,
        password_hash=generate_password_hash(password)
    )
    db_sess.add(user)
    db_sess.commit()



@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', encoding='utf8')


@app.route('/reviews')
def reviews():
    reviews = [{'images': [
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
        'text': 'YYYYeeeee haaaAaaaa'}, {'images': [
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
        'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'}, {'images': [],
        'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'},
        {'images': [
            'https://plus.unsplash.com/premium_photo-1677178660876-8578f4f6cbac?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
            'text': 'YYYYeeeeррррррррррррррррррррррррррррppppppppppppppppp3ррррррe ha'}]
    return render_template('reviews.html', encoding='utf8', reviews=reviews)


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'GET':
        return render_template('order.html', encoding='utf8')
    else:
        materials = {'2': 'Глянцевый', '1': 'Матовый'}
        colors = {'red': 'красный', 'green': 'зелёный', 'blue': 'синий', 'yellow': 'жёлтый', 'purple': 'фиолетовый', 'pink': 'розовый'}
        bot_send_order(request.form['width'], request.form['length'], materials[request.form['material']], request.form['lamps'], colors[request.form['colors']])
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        message.recipients = [form.email.data]
        print()
        user_info = {}
        user_info['surname'] = form.surname.data
        user_info['name'] = form.name.data
        user_info['sex'] = form.sex.data
        user_info['b_day'] = form.b_day.data
        user_info['email'] = form.email.data
        user_info['pwd'] = generate_password_hash(form.password.data)
        users_info[form.email.data] = user_info
        res = redirect('/verification')
        res.set_cookie(key='email', value=form.email.data, max_age=600)
        return res
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/verification', methods=['GET', 'POST'])
def verify():
    form = VerifyForm()
    email = request.cookies.get('email')
    if not form.is_submitted():
        code = randint(11111, 99999)
        users_info[email]['code'] = code
        message.body = f'Ваш код: {code}'
        mail.send(message)
        print(4)
    if form.validate_on_submit():
        code = users_info[email]['code']
        print(3)
        print(form.value.data, code)
        if int(form.value.data) == int(code):
            print(1)
            setup_user(users_info[email])
            res = redirect('/')
            res.delete_cookie(key='email')
            return res
        print(2)
        return render_template('register.html', title='Регистрация', message='Неверный код подтверждения', form=RegisterForm())
    return render_template('verification.html', title='Верификация', form=form)


if __name__ == '__main__':
    main()
