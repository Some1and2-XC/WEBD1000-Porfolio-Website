#!/usr/bin/env python

"""
File for Initializing the Webpage
# Gets all the requirements for building the app
"""

from flask import Flask
# from flask_login import LoginManager

from os import path
from os import environ

def create_app():
	import os
	import logging

	# from . import database

	logger = logging.getLogger(__name__)

	# App Configuration

	app = Flask(__name__)
	app.config["SECRET_KEY"] = os.urandom(12).hex()

	# Setting up Login Configuration

	# Login_Manager = SetupLogin(app)

	# Setting up Routes

	from .views.views import views
	# from .views.auth import auth
	# from .views.priv import priv

	# Register Routes

	app.register_blueprint(views, url_prefix = "/") # Registers views with the app
	# app.register_blueprint(auth, url_prefix = "/") # Registers auth with the app
	# app.register_blueprint(priv, url_prefix = "/") # Registers priv with the app

	return app

def SetupLogin(app):
	"""
	Function for Setting up Login Requirements
	"""
	from .database.DBCon import DBCTX
	from .models import User

	Login_Manager = LoginManager(app)
	Login_Manager.login_view = "auth.login"

	@Login_Manager.user_loader
	@DBCTX
	def LoadUser(UserID):
		"""
		Function for Loading a User in 
		"""

		from .database.DBCon import cur

		cur.execute("SELECT * FROM Users WHERE ID = (?)",[UserID])
		UserCurrent = cur.fetchone()
		if not UserCurrent: return None
		else: return User(*UserCurrent)

	return Login_Manager