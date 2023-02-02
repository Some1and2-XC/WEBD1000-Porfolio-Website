#!/usr/bin/env python3

from flask import abort
from flask_login import current_user
import functools

def AutoLogging(name):
	def decorator_constructor(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			import logging
			from flask import request
			from flask_login import current_user

			logger = logging.getLogger(f"{name}.{func.__name__}()")
			IPAddress = request.remote_addr

			# if current_user.is_authenticated: User = current_user.ID
			# else: User = "Anonymous"
			User = "None"

			logger.info(f"Page Request | UserID : {User} & IP : {IPAddress}")

			return func(*args, **kwargs)
		return wrapper
	return decorator_constructor