# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 06:50:58


from os import environ
from flask_migrate import Migrate
from sys import exit
from config import config_dict
from app import db, create_app

get_config_mode = environ.get('FLASK_ENV', 'development')

try:
    config_mode = config_dict[get_config_mode]
except KeyError:
    exit('Error: Invalid FLASK_ENV environment variable entry.')

app = create_app(config_mode)

Migrate(app, db)


if __name__ == "__main__":
	if get_config_mode == 'development':
	    app.run(host="0.0.0.0", port=5000)

	if get_config_mode == 'production':
	    app.run(host="127.0.0.1", port=5000)
