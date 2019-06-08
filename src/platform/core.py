#!/usr/bin/env python

from plugin_manifest import plugin_manifest

__author__ = "Robert Focke"
__copyright__ = "Copyright 2018-2019, Robert Focke"
__credits__ = ["Robert Focke"]
__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Robert Focke"
__email__ = "robert.focke@member.fsf.org"
__status__ = "Alpha"

class JobHandler:

	def __init__(self, job_type, job_data):
		self.job_type = job_type
		self.job_data = job_data

		# detect execution method from manifest
		self.execution_method = plugin_manifest[self.job_type]

	def result(self):
		return self.execution_method(
			self.job_data
		)
