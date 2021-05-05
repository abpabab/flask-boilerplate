# -*- coding: utf-8 -*-
# @Author: ubuntu
# @Date:   2021-04-23 05:50:17
# @Last Modified by:   ubuntu
# @Last Modified time: 2021-05-05 02:37:48


BAD_REQUEST = {
	"status": False,
	"code": 400,
	"message": "Bad request"
}

SERVER_ERR = {
	"status": False,
	"code": 500,
	"message": "Server error"
}

INVALID_USER = {
	"status": False,
	"code": 401,
	"message": "Invalid email or password"
}

VALID_USER = {
	"status": True,
	"code": 200,
	"message": "User login sucessfully"
}

def success(msg, data):
	return {
		"status": True,
		"message": msg,
		"data": data
	}