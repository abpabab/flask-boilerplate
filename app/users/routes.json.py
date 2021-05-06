# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-05 02:36:30


### ---For more security, consider to use bcrypt---
# from bcrypt import checkpw, hashpw, gensalt
### ---For demo or less security, use md5 from hashlib---
import hashlib
from flask import jsonify, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from app import app, db, login_manager
from app.users import blueprint
from app.users.models import User
from app.utils import responses


@blueprint.route('/', methods=['POST'], strict_slashes=False)
def register():
    """
    User register function
    """
    user_info = {}

    try:
        data = request.json

        user_info['username'] = data['username']
        user_info['password'] = data['password']
        user_info['name'] = data['name']
    except:
        return jsonify(responses.BAD_REQUEST), 400

    try:
        user_entity = User(user_info)
        db.session.add(user_entity)
        db.session.commit()

        del user_info['password']
        user_info['id'] = user_entity.id
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(responses.SERVER_ERR), 500

    return jsonify(responses.success(
            "User created sucessfully",
            user_info
        ))


@blueprint.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    User login function
    """

    # Check if user already logged in?
    if current_user.is_authenticated:
        return jsonify({
                "status": True,
                "message": "You are alredy logged in the system",
                "code": 200
            })
        # or return to the home page
        # return redirect(url_for('home_blueprint.index'))

    try:
        data = request.json

        username = data['username']
        password = hashlib.md5(data['password'].encode("utf-8")).hexdigest()
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(responses.BAD_REQUEST), 400

    user = User.query.filter_by(username=username).first()
    # if user and checkpw(password.encode("utf-8"), user.password): # bcrypt
    if user and password == user.password:                          # hashlib md5
        login_user(user)
    else:
        return jsonify(responses.INVALID_USER), 401

    return jsonify(responses.VALID_USER), 200


@blueprint.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    """
    User logout function
    """

    try:
        logout_user()
    except Exception as e:
        app.logger.error(str(e))
        return jsonify({
                "status": False,
                "code": 400,
                "message": "Bad request"
            })

    return jsonify({
        "status": True,
        "code": 200,
        "message": "You are logged out"
    })


@blueprint.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    """
    User change their password
    """


@blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    """
    This function generate <reset_token> for the user in a period time
    """


@blueprint.route('/setpassword/<token>', methods=['GET', 'POST'])
def reset_password_with_token(token):
    """
    Set new password if the <reset_token> is valid
    """
