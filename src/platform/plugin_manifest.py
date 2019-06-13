#!/usr/bin/env python

import plugins.time_series.historical_data_forecasting.fbprophet_forecasting as historical_data_forecasting
import plugins.language_processing.simple_text_processing.textblob_nlp as simple_text_processing

plugin_manifest = {
	"historical-data-forecasting": {
		"handler": historical_data_forecasting.handle_request,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/time_series/historical_data_forecasting/README.md"
	},
	"simple-text-processing": {
		"handler": simple_text_processing.handle_request,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/language_processing/simple_text_processing/README.md"
	}
}
