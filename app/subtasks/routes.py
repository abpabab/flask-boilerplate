# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 22:05:16
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-04 22:06:49


from flask import jsonify, redirect, request, url_for
from flask_login import (
    login_required
)
from app import app, db, login_manager
from app.subtasks import blueprint
from app.subtasks.models import SubTask
from app.utils import responses


@blueprint.route('/', methods=['GET'], strict_slashes=False)
@login_required
def get_all_subtasks():
    """
    Get all tasks
    """
    return jsonify("ok")
