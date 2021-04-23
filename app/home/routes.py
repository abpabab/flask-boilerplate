# -*- coding: utf8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:13
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 09:00:48


from app.home import blueprint
from flask import jsonify


@blueprint.route('/', methods=['GET'], strict_slashes=False)
def index():
    return jsonify({
                   'status': True,
                   'message': 'Home!'
                   })
