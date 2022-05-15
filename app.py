from flask import Flask, g, session
from flask_migrate import Migrate

from exts import db, mail
import config
from blueprints import qa_bp, user_bp
from models import UserModel, QuestionModel

#配置app 和 blueprint
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

@app.before_request
def check():
    if session.get('user_id'):
        try:
            user = UserModel.query.filter_by(id = session['user_id']).first()
            g.user = user
        except:
            g.user = None
    else:
        g.user = None

@app.context_processor
def cp():
    if g.user:
        return {'user':g.user}
    else:
        return {}


#配置数据库
db.init_app(app)
migrate = Migrate(app, db)

#配置邮箱
mail.init_app(app)

if __name__ == '__main__':
    app.run()
