#!/usr/bin/env python

import plugins.time_series.historical_data_forecasting.fbprophet_forecasting as historical_data_forecasting
import plugins.language_processing.simple_text_processing.textblob_nlp as simple_text_processing
import plugins.language_processing.language_understanding.snips_understanding as language_understanding

plugin_manifest = {
	"historical-data-forecasting": {
		"handler": historical_data_forecasting.handle_request,
		"cli": historical_data_forecasting.CLI,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/time_series/historical_data_forecasting/README.md"
	},
	"simple-text-processing": {
		"handler": simple_text_processing.handle_request,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/language_processing/simple_text_processing/README.md",
		"cli": simple_text_processing.CLI
	},
	"language-understanding":{
		"handler": language_understanding.handle_request,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/language_processing/language_understanding/README.md",
		"cli": language_understanding.CLI
	}
}
