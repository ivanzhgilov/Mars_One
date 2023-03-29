from flask import Flask, render_template, redirect, make_response, jsonify
from flask_login import login_user, LoginManager, logout_user, login_required, current_user
from flask_restful import Api
from sqlalchemy import select

from data import db_session
from data.users import User
from forms.login import LoginForm
from forms.user import RegisterForm
from routs import news_api, news_restful

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api.add_resource(news_restful.NewsListResource, '/api/v2/news')

api.add_resource(news_restful.NewsResource, '/api/v2/news/<int:news_id>')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/register', methods=['GET', 'POST'])
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
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route("/login")
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init('db/blogs.sqlite')
    db_sess = db_session.create_session()
    app.register_blueprint(news_api.blueprint)

    app.run(host='0.0.0.0', port=8000, debug=True)


#    user = User()
#    user.email = "myemail2@uriit.ru"
#    user.name = 'ioana'
#    user.about = ' lublu pelmeni'
#    user.hashed_password = "dodelati"
#    db_sess.add(user)
#    db_sess.commit()
#    users = db_sess.scalars(select(User))
#    for user in users:
#        print(user.name)

if __name__ == '__main__':
    main()
