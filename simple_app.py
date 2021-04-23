# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 21:28:39


from os import environ
from sys import exit
from config import config_dict
from app import create_app

get_config_mode = environ.get('FLASK_CONFIG', 'development')

try:
    config_mode = config_dict[get_config_mode]
except KeyError:
    exit('Error: Invalid FLASK_CONFIG environment variable entry.')

app = create_app(config_mode)

if get_config_mode == 'development':
    app.run(host="127.0.0.1, port=5000, debug=True)
