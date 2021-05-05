# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 21:09:36
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-04 21:10:11


from flask import Blueprint


blueprint = Blueprint(
    'tasks_blueprint',
    __name__,
    url_prefix='/tasks'
)
