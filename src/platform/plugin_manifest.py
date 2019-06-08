#!/usr/bin/env python

import plugins.time_series.fbprophet_forecasting as historical_data_forecasting

plugin_manifest = {
	"historical-data-forecasting": historical_data_forecasting.handle_request
}
