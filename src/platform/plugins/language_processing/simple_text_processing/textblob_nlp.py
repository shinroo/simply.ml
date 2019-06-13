#!/usr/bin/env python
#
# <simply.ml>
# ↳<NLP>
#  ↳< Simple Textual Analysis >
#
# [ job-type: simple-text-processing ]
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
import json

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
		'noun_phrases': noun_phrases
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
		parts_of_speech[str(pos_tuple[0])] = str(pos_tuple[1])

	return {
		'parts_of_speech': parts_of_speech
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

def word_tokenization(text):
	'''
	word_tokenization(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)
	
	words = []

	for word in temp.words:
		words.append(str(word))

	return {
		'words': words
	}

def sentence_tokenization(text):
	'''
	sentence_tokenization(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)

	sentences = []

	for sentence in temp.sentences:
		sentences.append(str(sentence))

	return {
		'sentences': sentences
	}

def word_frequencies(text):
	'''
	word_frequencies(text)

	parameters:
	- text

	returns:
	- dict
	'''
	tokenized = word_tokenization(text)
	tokens = tokenized['words']
	
	temp = TextBlob(text)

	frequencies = []

	for token in set(tokens):
		frequencies.append({
			"token": token,
			"frequency": temp.words.count(token)
		})

	return {
		'frequencies': frequencies
	}

def phrase_frequencies(text):
	'''
	phrase_frequencies(text)

	parameters:
	- text

	returns:
	- dict
	'''
	tokenized = noun_phrase_extraction(text)
	tokens = tokenized['noun_phrases']
	
	temp = TextBlob(text)

	frequencies = []

	for token in set(tokens):
		frequencies.append({
			"token": token,
			"frequency": temp.noun_phrases.count(token)
		})

	return {
		'frequencies': frequencies
	}

def spelling_correction(text):
	'''
	phrase_frequencies(text)

	parameters:
	- text

	returns:
	- dict
	'''
	temp = TextBlob(text)

	return {
		'correction': str(temp.correct())
	}

methods = {
	"noun-phrase-extraction": noun_phrase_extraction,
	"part-of-speech-tagging": part_of_speech_tagging,
	"sentiment-analysis": sentiment_analysis,
	"word-tokenization": word_tokenization,
	"sentence-tokenization": sentence_tokenization,
	"word-frequencies": word_frequencies,
	"phrase-frequencies": phrase_frequencies,
	"spelling-correction": spelling_correction
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

class CLI():

	def simple_text_processing(self, text, method):
		request = {
			"data": {
				"text": text
			},
			"options": {
				"method": method
			}
		}

		return json.dumps(handle_request(request), indent=4)
