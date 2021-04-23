# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:42:04
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 21:02:20


from flask import Blueprint


blueprint = Blueprint(
    'welcome_blueprint',
    __name__,
    url_prefix='/welcome'
)
