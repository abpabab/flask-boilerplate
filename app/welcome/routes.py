# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:13
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 09:01:15


from app.welcome import blueprint
from flask import jsonify


@blueprint.route('/', methods=['GET'], strict_slashes=False)
def index():
    return jsonify({
                   'status': True,
                   'message': 'Welcome to the API'
                   })
