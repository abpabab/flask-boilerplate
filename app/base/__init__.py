# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:34:11


from flask import Blueprint


blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='/'
)
