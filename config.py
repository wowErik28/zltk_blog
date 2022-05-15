#数据库信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlckqa'
USERNAME = 'root'
PASSWORD = '123.com'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

#
SECRET_KEY = "1122adhffuhusahdfu"

#邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1464873926@qq.com"
MAIL_PASSWORD = "cxqzgphevhttbaba"
MAIL_DEFAULT_SENDER = "1464873926@qq.com"