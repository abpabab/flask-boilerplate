# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-04 22:06:59


import pymysql
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import (
    basicConfig,
    getLogger,
    StreamHandler
    )


pymysql.install_as_MySQLdb()

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)


modules_list = ('home', 'users', 'base', 'tasks', 'subtasks')


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in (modules_list):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def configure_logs(app):
    filename = 'logs/error-' + str(app.config['ERR_LOG_LEVEL']) + '.log'
    basicConfig(filename=filename, level=app.config['ERR_LOG_LEVEL'])
    logger = getLogger()
    logger.addHandler(StreamHandler())


def create_app(config, selenium=False):
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)

    return app
