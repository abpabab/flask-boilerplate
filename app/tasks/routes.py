# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 21:09:43
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-05 03:47:07


from datetime import datetime
from flask import jsonify, redirect, request, url_for
from flask_login import (
    login_required
)
from app import app, db, login_manager
from app.tasks import blueprint
from app.tasks.models import Task
from app.utils import responses


task_status = {
    0: "New",
    1: "In progress",
    2: "Done",
    3: "Over due",
    4: "Closed"
}


@blueprint.route('/<_user_id>', methods=['GET'], strict_slashes=False)
@login_required
def get_all_tasks(_user_id):
    """
    Get all tasks belong to user
    by <user_id>
    """

    tasks = []

    try:
        user_id = int(_user_id)
    except:
        return jsonify(responses.BAD_REQUEST), 400

    query = Task.query.filter_by(user_id=user_id).all()
        
    if not query:
        return jsonify(responses.NOT_FOUND), 404

    for q in query:
        del q._sa_instance_state
        tasks.append(q.__dict__)

    return jsonify(responses.success(
                "Get all tasks of user_id: " + str(user_id),
                tasks
           ))


@blueprint.route('/<_user_id>/<_task_id>', methods=['GET'], strict_slashes=False)
@login_required
def get_one_task(_user_id, _task_id):
    """
    Get one task belong to user
    by <user_id> and <task_id>
    """

    try:
        user_id = int(_user_id)
        task_id = int(_task_id)
    except:
        return jsonify(responses.BAD_REQUEST), 400

    task = Task.query.filter_by(user_id=user_id, id=task_id).first()
    
    if not task:
        return jsonify(responses.NOT_FOUND), 404

    del task._sa_instance_state

    return jsonify(responses.success(
                "Get task_id: " + str(task_id) + " of user_id: " + str(user_id),
                task.__dict__
           ))


@blueprint.route('/<_user_id>', methods=['POST'], strict_slashes=False)
@login_required
def create_task(_user_id):
    """
    Create one task belong to user
    by <user_id>
    """

    task_info = {}

    try:
        data = request.json

        task_info['user_id'] = int(data['user_id'])
        task_info['name'] = str(data['name'])
        task_info['description'] = str(data['description'])
        task_info['due_date'] = datetime.strptime(str(data['due_date']), '%Y-%m-%d %H:%M')
    except:
        return jsonify(responses.BAD_REQUEST), 400

    try:
        task_entity = Task(task_info)
        db.session.add(task_entity)
        db.session.commit()
    except Exception as e:
        app.logger.error(str(e))
        return jsonify(responses.SERVER_ERR), 500

    return jsonify(responses.success(
            "Task created sucessfully",
            task_info
        ))


@blueprint.route('/<_user_id>/<_task_id>/status', methods=['GET'], strict_slashes=False)
@login_required
def get_task_status(_user_id, _task_id):
    """
    Get task status belong to user
    by <user_id> and <task_id>
    """

    try:
        user_id = int(_user_id)
        task_id = int(_task_id)
    except:
        return jsonify(responses.BAD_REQUEST), 400

    task = Task.query.filter_by(user_id=user_id, id=task_id).first()

    if not task:
        return jsonify(responses.NOT_FOUND), 404

    status = task_status[task.status]

    return jsonify(responses.success(
                "Status of task_id: " + str(task_id) + " and user_id: " + str(user_id),
                {"task_status": status}
           ))



@blueprint.route('/<_user_id>/<_task_id>/status', methods=['PUT'], strict_slashes=False)
@login_required
def update_one_task(_user_id, _task_id):
    """
    Update one task belong to user
    by <user_id> and <task_id>
    """

    try:
        user_id = int(_user_id)
        task_id = int(_task_id)
    except:
        return jsonify(responses.BAD_REQUEST), 400

    # Validate task update input
    try:
        data = request.json

        new_status = int(data['status'])
        new_status_string = task_status[new_status]
    except:
        return jsonify(responses.BAD_REQUEST), 400

    task = Task.query.filter_by(user_id=user_id, id=task_id).first()
    
    if not task:
        return jsonify(responses.NOT_FOUND), 404

    task.status = new_status          # change the status to <new_status>
    task_copy = task.__dict__.copy()  # to return to the user because task will be destroy after db.session.commit()
    db.session.commit()

    del task_copy['_sa_instance_state']

    return jsonify(responses.success(
                "Update task_id: " + str(task_id) + " and user_id: " + str(user_id),
                task_copy
           ))