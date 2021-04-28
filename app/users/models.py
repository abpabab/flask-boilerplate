# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:42:56
# @Last Modified by:   abpabab
# @Last Modified time: 2021-04-26 06:32:52


### ---For more security, consider to use bcrypt---
# from bcrypt import checkpw, hashpw, gensalt
### ---For demo or less security, use md5 from hashlib---
import hashlib
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import (
    Integer,
    BINARY,
    DateTime,
    String
    )
from app import db, login_manager


class User(db.Model, UserMixin):
    """
    User model
    """

    __tablename__ = 'users'

    id                = db.Column(Integer, primary_key=True)
    username          = db.Column(String(100), unique=True, nullable=False)
    ### ---len(md5 hash) == 32---
    password          = db.Column(String(32), nullable=False)
    name              = db.Column(String(50), nullable=False)
    created_time      = db.Column(DateTime, default=datetime.utcnow)
    updated_time      = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, user_data):
        for key, value in user_data.items():
            if key == 'password':
                # value = hashpw(value.encode("utf-8"), gensalt())     # bcrypt
                value = hashlib.md5(value.encode("utf-8")).hexdigest() # hashlib md5
            setattr(self, key, value)

    def __repr__(self):
        return str(self.username)


"""
user_loader will looking for the "Cookies" header
for authentication
"""
@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))


"""
request_loader, however, not looking for the "Cookies" header
this is the way to customize the authentication method
ex: Authorization header in the JWT usage
great explaination here: https://gouthamanbalaraman.com/blog/minimal-flask-login-example.html
"""
@login_manager.request_loader
def request_loader(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":") # naive token
        user_entry = User.get(username)
        if (user_entry is not None):
            user = User(user_entry[0],user_entry[1])
            if (user.password == password):
                return user
    return None
