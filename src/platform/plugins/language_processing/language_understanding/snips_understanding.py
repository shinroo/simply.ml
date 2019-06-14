#!/usr/bin/env python
#
# <simply.ml>
# ↳<NLP>
#  ↳< Natural Language Understanding >
#
# [ job-type: language-understanding ]
#
# Parse sentences written in natural language and 
# extract structured information
#
# Powered by: Snips NLU (Apache 2.0)
# https://github.com/snipsco/snips-nlu
#
# Inputs:
#
# {
#   "data": {
#     "training_json_url": "http://dataset.json",
#     "text": "Turn the lights on"
#   },
#   "options": {
#     "language": "en"
#   }
# }

# standard libs
from __future__ import unicode_literals, print_function
import json
import io
import urllib.request
import os
import uuid

# 3rd party libs
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

# local files

# meta information
__author__ = "Robert Focke"
__copyright__ = "Copyright 2018-2019, Robert Focke"
__credits__ = ["Robert Focke"]
__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Robert Focke"
__email__ = "robert.focke@member.fsf.org"
__status__ = "Alpha"

def download_json(url, outfile_name):
	'''
	download_json(url, outfile_name)

	parameters:
	- url: string (the url of a json like file)
	- outfile_name: the name of the file to write
	   downloaded csv data to for temporary
	   storage
	'''
	json = urllib.request.urlopen(url).read()
	with open(outfile_name, 'wb') as outfile:
		outfile.write(json)

def delete_file(filename):
	'''
	delete_file(filename)

	parameters:
	- filename: string
	'''
	os.remove(filename)

def generate_filename():
	'''
	generate_filename()

	returns:
	- filename based on uuid4
	'''
	return f'{uuid.uuid4()}.json'

def handle_request(request):
	filename = generate_filename()
	download_json(
		request['data']['training_json_url'],
		filename
	)

	with io.open(filename) as f:
		sample_dataset = json.load(f)

	nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
	nlu_engine = nlu_engine.fit(sample_dataset)
	parsing = nlu_engine.parse(request['data']['text'])

	delete_file(filename)

	return parsing

handle_request({
	'data': {
		'training_json_url': 'https://raw.githubusercontent.com/snipsco/snips-nlu/develop/sample_datasets/lights_dataset.json',
		'text': 'Turn the lights on in the kitchen'
	},
	'options': {
		'language': 'en'
	}
})

class CLI():

	def language_understanding(self, training_url, text, language):
		request = {
			'data': {
				'training_json_url': str(training_url),
				'text': str(text)
			},
			'options': {
				'language': str(language)
			}
		}

		return json.dumps(handle_request(request), indent=4)
