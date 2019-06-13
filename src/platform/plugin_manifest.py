#!/usr/bin/env python

import plugins.time_series.historical_data_forecasting.fbprophet_forecasting as historical_data_forecasting

plugin_manifest = {
	"historical-data-forecasting": {
		"handler": historical_data_forecasting.handle_request,
		"docs": "https://github.com/shinroo/simply.ml/blob/master/src/platform/plugins/time_series/historical_data_forecasting/README.md"
	}
}
