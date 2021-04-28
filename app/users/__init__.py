# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:49:40
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 05:50:06


from flask import Blueprint


blueprint = Blueprint(
    'users_blueprint',
    __name__,
    url_prefix='/users'
)
