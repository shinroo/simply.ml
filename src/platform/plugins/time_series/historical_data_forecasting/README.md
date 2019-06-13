# Forecasting From Historical Data

**category:** `time-series`

**job_type:** `historical-data-forecasting`

**powered_by:** `Prophet` (MIT): [Repo](https://github.com/facebook/prophet)

Producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth.

## Data Definition

### POST Request

Incoming Request:

```json
{
	"data": {
		"training_csv_url": "http://my.url/csv",
		"prediction_frequency": "daily"
	},
	"options": {
		"csv_delimiter": ",",
		"date_format_string": "%Y-%m-%d"
	}
}
```

Monthly, Yearly, Weekly coming soon!

### CSV Format

|df|y|
|--|--|
|1996-04-25|9.12393|

