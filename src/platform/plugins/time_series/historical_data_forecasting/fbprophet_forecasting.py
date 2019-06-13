#!/usr/bin/env python
#
# <simply.ml>
# ↳<TSA>
#  ↳< Forecasting From Historical Data >
#
# [ job-type: historical-data-forecasting ]
#
# Producing high quality forecasts for time series data that 
# has multiple seasonality with linear or non-linear growth.
#
# Powered by: Prophet (MIT)
# https://github.com/facebook/prophet
#
# Inputs:
#
# {
# 	"data": {
# 		"training_csv_url": "http://my.url/csv",
# 		"prediction_frequency": "daily"
# 	}
# 	"options": {
# 		"csv_delimiter": ",",
# 		"date_format_string": "%Y-%m-%d"
# 	}
# }

# standard libs
import urllib.request
import uuid
import os
import json
import time
import datetime

# 3rd party libs
import pandas as pd
from fbprophet import Prophet
import pytest

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

def download_csv(url, outfile_name):
	'''
	download_csv(url, outfile_name)

	parameters:
	- url: string (the url of a csv like file)
	- outfile_name: the name of the file to write
	   downloaded csv data to for temporary
	   storage
	'''
	csv = urllib.request.urlopen(url).read()
	with open(outfile_name, 'wb') as outfile:
		outfile.write(csv)

def delete_file(filename):
	'''
	delete_file(filename)

	parameters:
	- filename: string
	'''
	os.remove(filename)

def get_last_stamp(df):
	'''
	get_last_stamp(df)

	parameters:
	- df

	returns:
	- last date in data frame, representing date
	   to filter after
	'''
	return df['ds'].tail(1).iloc[0]

def read_csv_into_df(filename, delimiter):
	'''
	read_csv_into_df(filename)

	parameters:
	- filename: string
	- delimiter: character

	returns:
	- pandas data frame representing
	   contents of file
	'''
	df = pd.read_csv(filename, delimiter=delimiter)
	return df

def fit_model(df):
	'''
	fit_model(df)

	parameters:
	- df: pandas dataframe with 2 headings (ds, y)

	returns:
	- Prophet model fit to the dataframe
	'''
	model = Prophet()
	return model.fit(df)

def predict_future(model, frequency):
	'''
	predict_future(model, frequency)

	parameters:
	- model: Prophet model
	- frequency: number of periods to extend data
	   frame

	returns:
	- pandas dataframe with ds extended into the 
	   future
	'''
	future_df = model.make_future_dataframe(periods=frequency)
	forecast = model.predict(future_df)
	return forecast

def generate_filename():
	'''
	generate_filename()

	returns:
	- filename based on uuid4
	'''
	return f'{uuid.uuid4()}.csv'

def map_prediction_frequency(frequency):
	'''
	map_prediction_frequency(frequency)

	parameters:
	- daily | monthly | yearly

	returns:
	- number of periods to extend data
	   frame by
	'''
	if frequency not in ['daily', 'monthly', 'yearly']:
		raise Exception('unknown frequency')

	frequency_map = {
		"daily": 365,
		"monthly": 12,
		"yearly": 1
	}

	return frequency_map[frequency]

def filter_output_only_predictions(prediction_json, filter_date, date_format_string):
	'''
	filter_output_only_predictions(prediction_json, filter_date, date_format_string)

	parameters:
	- prediction_json
	- filter pivot date, dates <= pivot will be excluded from output
	- date format string

	returns
	- filtered prediction_json
	'''
	pivot_date = datetime.datetime.strptime(filter_date, date_format_string)

	def validate(item):
		check_date = datetime.datetime.strptime(
			item['time_stamp'],
			date_format_string
		)

		if check_date > pivot_date:
			return True
		else:
			return False

	return_json = [
		item for item in prediction_json if validate(item)
	]

	return return_json

def export_dataframe_as_json(df):
	'''
	export_dataframe_as_json(df)

	parameters:
	- df: pandas dataframe

	returns:
	- dict
	'''
	return json.loads(
		df.to_json(orient='records',lines=False)
		.replace('ds','time_stamp')
		.replace('yhat','value')
	)

def handle_request(request):
	'''
	handle_request(request)

	parameters:
	- request: dict

	{
		"data": {
			"training_csv_url": "http://my.url/csv",
			"prediction_frequency": "daily|monthly|yearly"
		}
		"options": {
			"csv_delimiter": ",",
			"date_format_string": "%Y-%m-%d"
		}
	}

	returns:
	- list of dicts representing original dataframe
	   + predicted future values
	'''
	# prepare needed data
	try:
		filename = generate_filename()
		url = request['data']['training_csv_url']
	except Exception as e:
		print(e)
		exit(1)

	# process
	try:
		# retrieve CSV
		print("downloading csv...")
		download_csv(url, filename)
		print("done!")

		# convert to pandas data frame
		print("reading csv data...")
		df = read_csv_into_df(
			filename,
			request['options']['csv_delimiter']
		)

		# retrieve last_stamp 
		print("inferring last date from CSV data...")
		last_stamp = get_last_stamp(df)

		# fit facebook model
		print("fitting model...")
		model = fit_model(df)

		# forecast data
		print("forecasting...")
		forecast = predict_future(
			model,
			map_prediction_frequency(
				request['data']['prediction_frequency']
			)
		)

		# convert unix stamps to formatted date strings
		print("cleaning data...")
		forecast['ds'] = forecast['ds'].dt.strftime(
			request['options']['date_format_string']
		)
		
	except Exception as e:
		print(e)
		exit(2)

	# create output
	try:
		# convert data frame to json
		print("exporting as json...")
		prediction_json =  export_dataframe_as_json(
			forecast.drop(
				columns = [
					'trend', 'yhat_lower', 'yhat_upper', 
					'trend_lower', 'trend_upper','additive_terms',
					'additive_terms_lower','additive_terms_upper','weekly',
					'weekly_lower','weekly_upper','yearly',
					'yearly_lower','yearly_upper','multiplicative_terms',
					'multiplicative_terms_lower','multiplicative_terms_upper'
				]
			)
		)
	except Exception as e:
		print(e)
		exit(3)

	# filter output (only predictions)
	try:
		print("filtering to retrieve only predictions...")
		prediction_json = filter_output_only_predictions(
			prediction_json,
			last_stamp,
			request['options']['date_format_string']
		)
	except Exception as e:
		print(e)
		exit(4)

	# cleanup temp files
	try:
		print("delete temp files...")
		delete_file(filename)
	except Exception as e:
		print(e)
		exit(5)

	print(json.dumps(prediction_json, indent=4))

	return prediction_json
