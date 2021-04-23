# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-22 21:01:21


class Config(object):
    """
    Base Config class
    """

    ERR_LOG_LEVEL = 'ERROR'


class ConfigProduction(Config):
    """
    Production config set
    """


class ConfigDevelopment(Config):
    """
    Development config set
    --only for development and testing--
    """


config_dict = {
    'production': ConfigProduction,
    'development': ConfigDevelopment
}
