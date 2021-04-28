# -*- coding: utf8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:13
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 09:00:48


from app.home import blueprint
from flask import jsonify
from flask_login import login_required


@blueprint.route('/', methods=['GET'], strict_slashes=False)
@login_required
def index():
    return jsonify({
                   'status': True,
                   'code': 200,
                   'message': 'Home!'
                   }), 200
