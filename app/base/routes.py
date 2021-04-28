# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:33:41


from flask import (
    jsonify,
    redirect,
    url_for)

from app import app, login_manager
from app.base import blueprint


@blueprint.route('/', methods=['GET'])
def route_default():
    return redirect(url_for('user_blueprint.login'))


@app.login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify({
                   "status": False,
                   "code": 401,
                   "message": "Unauthorized request access"
                   }), 401


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
                   "status": False,
                   "code": 400,
                   "message": "Bad user request"
                   }), 400


@app.errorhandler(403)
def access_forbidden(error):
    return jsonify({
                   "status": False,
                   "code": 403,
                   "message": "Access is not permitted"
                   }), 403


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
                   "status": False,
                   "code": 404,
                   "message": "Access resource does not exist"
                   }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
                   "status": False,
                   "code": 500,
                   "message": "Server error"
                   }), 500
