# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 22:05:11
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-05 03:50:58


from datetime import datetime
from sqlalchemy import (
    Integer,
    DateTime,
    String,
    Text
    )
from app import db


class SubTask(db.Model):
    """
    Subtask model
    """

    __tablename__ = 'subtasks'

    id                = db.Column(Integer, primary_key=True)
    task_id           = db.Column(Integer, db.ForeignKey('tasks.id'), nullable=False)
    name              = db.Column(String(100), nullable=False)
    description       = db.Column(Text, nullable=False)
    due_date          = db.Column(DateTime, nullable=False)
    status            = db.Column(Integer, default=0, nullable=False)
    created_time      = db.Column(DateTime, default=datetime.utcnow)
    updated_time      = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)