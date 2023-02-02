#!/usr/bin/env python

"""
File for managing the main views for the website
"""

from flask import Blueprint # Blueprints lets you split up views into multiple files cleanly
from flask import render_template
from flask import request
from flask import flash
from flask import send_from_directory

# from flask_login import login_required, current_user

from ..wrappers import AutoLogging

views = Blueprint("views", __name__)

@views.route("/", methods = ["GET", "POST"])
@AutoLogging(__name__)
def home():
	"""
	View for Homepage
	"""

	return render_template("index.html")

@views.route("/goals", methods = ["GET", "POST"])
@AutoLogging(__name__)
def goals():
	"""
	View for Goals page
	"""

	return render_template("goals.html")

@views.route("/skills", methods = ["GET", "POST"])
@AutoLogging(__name__)
def skills():
	"""
	View for Skills Page
	"""

	return render_template("skills.html")

@views.route("/resume", methods = ["GET", "POST"])
@AutoLogging(__name__)
def resume():
	"""
	View for Resume Page
	"""

	return render_template("resume.html")

@views.route("/contact", methods = ["GET", "POST"])
@AutoLogging(__name__)
def contact():
	"""
	View for contact Page
	"""

	return render_template("contact.html")
