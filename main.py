from flask import Flask, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message, Mail
from forms import LoginForm, RegisterForm, VerifyForm
from data import db_session
from data.users import User
from data.reviews import Review
from bot import bot_send_order
from flask_login import login_user, LoginManager, login_required, logout_user, current_user, AnonymousUserMixin
from random import randint
from dotenv import load_dotenv
import os

load_dotenv('.env')


app = Flask(__name__, template_folder='static/templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
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
        password_hash=generate_password_hash(password),
        pwd=password
    )
    db_sess.add(user)
    db_sess.commit()


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', encoding='utf8')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/reviews')
def reviews():
    db_sess = db_session.create_session()
    res = db_sess.query(User.name, User.surname, Review).filter(User.id == Review.user_id)
    reviews = []
    for name, surname, review in res:
        img = str(review.img).split(';')
        if img == ['']:
            img = []
        a = {'name': name+' '+surname, 'rating': review.rating, 'text': review.text, 'images': img, 'user': review.user, 'id': review.id}
        print(a)
        reviews.append(a)
        a = {}
    show = False
    if not isinstance(current_user, AnonymousUserMixin) and current_user.is_ordered and not current_user.made_review:
        show = True
    return render_template('reviews.html', encoding='utf8', reviews=reviews, show=show)

@app.route('/make_review', methods=['GET', 'POST'])
@login_required
def make_review():
    if request.method == 'GET':
        return render_template('/make_review.html', maden=False)
    else:
        stars = 6 - int(request.form['rating'])
        text = request.form['text']
        files = request.files.getlist('review_load_image')
        data = []
        for file in files:
            print(file)
            if file.filename:
                with open('static/users_img/'+file.filename, 'wb') as new_file:
                    new_file.write(file.read())
                data.append('static/users_img/'+file.filename)
        db_sess = db_session.create_session()
        review = Review()
        review.text = text
        review.rating = int(stars)
        review.user = current_user
        review.img = ';'.join(data)

        current_user.reviews.append(review)
        db_sess.merge(current_user)
        db_sess.commit()
        return render_template('/make_review.html', maden=True)


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'GET':
        return render_template('order.html', encoding='utf8')
    else:
        materials = {'2': 'Глянцевый', '1': 'Матовый'}
        colors = {'red': 'красный', 'green': 'зелёный', 'blue': 'синий', 'yellow': 'жёлтый', 'purple': 'фиолетовый',
                  'pink': 'розовый'}
        bot_send_order(request.form['width'], request.form['length'], materials[request.form['material']],
                       request.form['lamps'], colors[request.form['colors']])
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
        user_info = {}
        user_info['surname'] = form.surname.data
        user_info['name'] = form.name.data
        user_info['sex'] = form.sex.data
        user_info['b_day'] = form.b_day.data
        user_info['email'] = form.email.data
        user_info['pwd'] = form.password.data
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
    if form.validate_on_submit():
        code = users_info[email]['code']
        if int(form.value.data) == int(code):
            setup_user(users_info[email])
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == email).first()
            login_user(user)
            res = redirect('/')
            res.delete_cookie(key='email')
            return res
        return render_template('register.html', title='Регистрация', message='Неверный код подтверждения', form=RegisterForm())
    return render_template('verification.html', title='Верификация', form=form)


@app.route('/change_review/<int:id>', methods=['GET', 'POST'])
def change_review(id):
    if request.method == 'GET':
        return render_template('change_review.html', changed=False)
    return render_template('change_review.html', changed=True)

if __name__ == '__main__':
    main()
