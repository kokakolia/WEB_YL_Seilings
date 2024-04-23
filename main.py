from flask import Flask, render_template, redirect, request
from werkzeug.security import generate_password_hash
import datetime
from loginform import LoginForm
from data import db_session
from data.users import User


app = Flask(__name__, template_folder='static/templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/userdata.db')
    app.run(port=8080, host='127.0.0.1')


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


@app.route('/order')
def order():
    return render_template('order.html', encoding='utf8')


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
