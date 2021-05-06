# -*- coding: utf8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:13
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 09:00:48


from app.home import blueprint
from flask import (
    jsonify, 
    render_template
)
from flask_login import login_required


@blueprint.route('/<user_id>', methods=['GET'], strict_slashes=False)
@login_required
def index(user_id):
    
    return render_template('home.html', user_id=user_id)