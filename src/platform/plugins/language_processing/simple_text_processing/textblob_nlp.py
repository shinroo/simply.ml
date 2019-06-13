#!/usr/bin/env python
#
# <simply.ml>
# ↳<NLP>
#  ↳< Simple Textual Analysis >
#
# [ job-type: simple-text-processing ]
#
# Producing high quality forecasts for time series data that 
# has multiple seasonality with linear or non-linear growth.
#
# Common natural language processing (NLP) tasks such as 
# part-of-speech tagging, noun phrase extraction, 
# sentiment analysis, classification, translation, and more.
#
# Powered by: TextBlob (MIT)
# https://github.com/sloria/TextBlob
#
# Inputs:
#
# {
#   "data": {
#     "text": "Example text"
#   },
#   "options": {
#     "method": "method-key"
#   }
# }

# standard libs

# 3rd party libs
from textblob import TextBlob

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

def noun_phrase_extraction(text):
	'''
	noun_phrase_extraction(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)
	
	noun_phrases = []

	for phrase in temp.noun_phrases:
		noun_phrases.append(phrase)

	return {
		'noun_phrases': noun_phrases,
		'description': 'Returns a list of noun phrases found in the provided text'
	}

methods = {
	"noun-phrase-extraction": noun_phrase_extraction
#	"part-of-speech-tagging": ,
#	"sentiment-analysis": ,
#	"classification": ,
#	"tokenization": ,
#	"frequencies": ,
#	"parsing": ,
#	"n-gram": ,
#	"inflection-lemmatization": ,
#	"spelling-correction":
}

def handle_request(request):
	'''
	handle_request(request)

	parameters:
	- request: dict

	{
		"data": {
			"text": "Example text"
		},
		"options": {
			"method": "method-key"
		}
	}

	returns:
	- response: dict
	'''

	return methods[request['options']['method']](
		request['data']['text']
	)