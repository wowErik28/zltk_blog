from datetime import datetime

from flask import Blueprint, render_template, request, redirect, \
    url_for, session, flash, g
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from exts import mail
from .forms import RegisterForm, LoginForm, QuestionForm
from models import db, UserModel, QuestionModel
from decorators import login_required

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))

@bp.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form)
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('qa.index'))
        flash('邮箱或者密码错误')
        return render_template('login.html')

@bp.route('/register', methods=['POST', "GET"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate():
            #保存到数据库
            email = form.email.data
            username = form.username.data
            password = generate_password_hash(form.password.data)
            user = UserModel(email=email, username=username, password=password,
                             join_time=datetime.now())
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return render_template('register.html')

@bp.route('/mail')
def send_mail():
    message = Message('邮箱测试',
                      recipients=['3574068495@qq.com'],
                      body='这是邮件测试')
    mail.send(message)
    return "success"

@bp.route('/question/public', methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content,
                          create_time=datetime.now(), author_id=g.user.id)

            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            return render_template('public_question.html')

