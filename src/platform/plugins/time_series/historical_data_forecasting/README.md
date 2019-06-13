# Forecasting From Historical Data

**category:** `time-series`

**job_type:**`numerical-data-forecasting`

Producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth.

API: `https://api.simply.ml/v1.0/job/time-series/numerical-data-forecasting` `POST`

Demo: `https://demo.simply.ml/time-series/numerical-data-forecasting`

## Data Definition

### POST Request

Incoming Request:

```json
{
	"data": {
		"training_csv_url": "http://my.url/csv",
		"prediction_frequency": "daily"
	}
	"options": {
		"csv_delimiter": ",",
		"date_format_string": "%Y-%m-%d"
	}
}
```

Monthly, Yearly, Weekly also possible

### CSV Format

|df|y|
|--|--|
|1996-04-25|9.12393|

