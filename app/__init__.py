# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 21:02:03


from flask import Flask
from importlib import import_module
from logging import basicConfig, getLogger, StreamHandler


app = Flask(__name__)


def register_blueprints(app):
    for module_name in ('home', 'welcome'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    filename = 'logs/error-' + str(app.config['ERR_LOG_LEVEL']) + '.log'
    basicConfig(filename=filename, level=app.config['ERR_LOG_LEVEL'])
    logger = getLogger()
    logger.addHandler(StreamHandler())


def create_app(config):
    app.config.from_object(config)

    register_blueprints(app)
    configure_logs(app)

    return app
