#!/usr/bin/env python

# Main file for Configuring website data, main file to run to spin up website

from . import create_app # runs `create_app()` function from `website` directory

app = create_app()

if __name__ == "__main__":
	app.run(debug = True) # Sets up the Webserver

