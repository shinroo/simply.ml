#!/usr/bin/env python

import connexion
import json
from core import JobHandler

# meta information
__author__ = "Robert Focke"
__copyright__ = "Copyright 2018-2019, Robert Focke"
__credits__ = ["Robert Focke"]
__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Robert Focke"
__email__ = "robert.focke@member.fsf.org"
__status__ = "Alpha"

def handle_job_submission(job_type: str) -> dict:
	handler = JobHandler(
		job_type,
		connexion.request.json
	)

	return handler.result()

if __name__ == '__main__':
	# create app
	app = connexion.FlaskApp(
		__name__,
		port=8080,
		specification_dir='api/',
		debug=True
	)

	# load api specifcations
	app.add_api(
		'job.yaml',
		arguments={
			'title': 'Job submission'
		}
	)

	# run app
	app.run()