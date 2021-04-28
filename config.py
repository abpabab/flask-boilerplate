# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-22 08:31:53
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-04-23 05:41:16


class Config(object):
    """
    Base Config class
    """

    SECRET_KEY = "Very random string here to make more strength"

    ERR_LOG_LEVEL = 'ERROR'


class ConfigProduction(Config):
    """
    Production config set
    """

    SQLALCHEMY_DATABASE_URI = 'mysql://prod_user:prod_password@localhost/prod_db?use_unicode=1&charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigDevelopment(Config):
    """
    Development config set
    --only for development and testing--
    """

    SQLALCHEMY_DATABASE_URI = 'mysql://dev_user:dev_password@localhost/dev_db?use_unicode=1&charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_dict = {
    'production': ConfigProduction,
    'development': ConfigDevelopment
}
