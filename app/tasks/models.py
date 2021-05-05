# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-05-04 21:09:49
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-05 03:50:35


from datetime import datetime
from sqlalchemy import (
    Integer,
    DateTime,
    String,
    Text
    )
from app import db


class Task(db.Model):
    """
    Task model
    """

    __tablename__ = 'tasks'

    id                = db.Column(Integer, primary_key=True)
    user_id           = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name              = db.Column(String(100), nullable=False)
    description       = db.Column(Text, nullable=False)
    due_date          = db.Column(DateTime, nullable=False)
    status            = db.Column(db.Integer, default=0, nullable=False)
    created_time      = db.Column(DateTime, default=datetime.utcnow)
    updated_time      = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)