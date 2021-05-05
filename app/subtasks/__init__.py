# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 22:05:06
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-04 22:05:36


from flask import Blueprint


blueprint = Blueprint(
    'subtasks_blueprint',
    __name__,
    url_prefix='/subtasks'
)
