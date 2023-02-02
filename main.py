#!/usr/bin/env python

# Main file for Configuring website data, main file to run to spin up website

from website import create_app # runs `create_app()` function from `website` directory

app = create_app()

if __name__ == "__main__":

	import logging
	import logging.config

	logging.config.fileConfig("logging.ini", disable_existing_loggers=False)

	logger = logging.getLogger("waitress")
	logger.setLevel(logging.DEBUG)

	app.run(host = "127.0.0.1", port = 80, debug = True) # Sets up the Webserver for development