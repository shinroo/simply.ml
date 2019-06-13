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
		self.plugin_manifest = plugin_manifest
		self.job_type = job_type
		self.job_data = job_data

		# detect execution method from manifest
		self.execution_method = self.plugin_manifest[self.job_type]['handler']

	def result(self):
		return self.execution_method(
			self.job_data
		)

class JobTypesHandler:

	def __init__(self):
		self.plugin_manifest = plugin_manifest

		temp_l = []

		for key in plugin_manifest.keys():
			temp_l.append(key)

		self.job_types = temp_l

	def get_job_types(self):
		return {
			'job_types': self.job_types
		}

class JobDocsHandler:

	def __init__(self, job_type):
		self.plugin_manifest = plugin_manifest
		self.job_type = job_type

	def get_docs(self):
		return {
			'docs': self.plugin_manifest[self.job_type]['docs']
		}
