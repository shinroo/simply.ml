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

def part_of_speech_tagging(text):
	'''
	part_of_speech_tagging(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)
	
	parts_of_speech = {}

	for pos_tuple in temp.tags:
		print(pos_tuple[0])
		parts_of_speech[str(pos_tuple[0])] = str(pos_tuple[1])

	return {
		'parts_of_speech': parts_of_speech,
		'description': 'Returns a dictionary representing each word in the provided text with its corresponding part of speech'
	}

def sentiment_analysis(text):
	'''
	sentiment_analysis(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)

	return {
		"description": "Returns values for the polarity (positive/negative) and subjectivity (subjective/objective) for the provided text",
		"ranges": {
			"polarity": {
				"lower_bound": "-1.0 (Negative)",
				"upper_bound": "1.0 (Positive)"
			},
			"subjectivity": {
				"lower_bound": "0.0 (Very Objective)",
				"upper_bound": "1.0 (Very Subjective)"
			}
		},
		"polarity": temp.sentiment.polarity,
		"subjectivity": temp.sentiment.subjectivity
	}

def tokenization(text):
	'''
	tokenization(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)
	
	words = []

	for word in temp.words:
		words.append(str(word))

	sentences = []

	for sentence in temp.sentences:
		sentences.append(str(sentence))

	return {
		'words': words,
		'sentences': sentences,
		'description': 'Returns a dictionary representing words and sentences found in the provided text.'
	}

methods = {
	"noun-phrase-extraction": noun_phrase_extraction,
	"part-of-speech-tagging": part_of_speech_tagging,
	"sentiment-analysis": sentiment_analysis,
	"tokenization": tokenization,
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
