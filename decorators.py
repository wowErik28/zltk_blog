from functools import wraps

from flask import g, redirect, url_for

#要求用户必须为登录状态
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user:
                return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))

    return wrapper