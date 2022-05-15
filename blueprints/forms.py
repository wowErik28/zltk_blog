import wtforms
from wtforms.validators import length, email, EqualTo

from models import UserModel

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(6, 20)])

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(1, 20)])
    username = wtforms.StringField(validators=[length(1, 20)])
    password = wtforms.StringField(validators=[length(6, 20)])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])

    #判断是否有重复email
    def validate_email(self, field):
        email = field.data
        result = UserModel.query.filter_by(email=email).first()
        if result:
            raise wtforms.ValidationError('存在email')

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(1, 50)])
    content = wtforms.StringField(validators=[length(min=5)])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
