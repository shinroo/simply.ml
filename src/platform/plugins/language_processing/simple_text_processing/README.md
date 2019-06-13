# Simple Text Processing

**category:** `language-processing`

**job_type:** `simple-text-processing`

**powered_by:** `TextBlob` (MIT): [Repo](https://github.com/sloria/TextBlob)

Producing high quality forecasts for time series data that has multiple seasonality with linear or non-linear growth.

## Methods

|Method Name|Method Key|
|-----------|----------|
|Noun phrase extraction|noun-phrase-extraction|
|Part-of-speech tagging|part-of-speech-tagging|
|Sentiment analysis|sentiment-analysis|
|Classification (Naive Bayes, Decision Tree)|classification|
|Tokenization (splitting text into words and sentences)|tokenization|
|Word and phrase frequencies|frequencies|
|Parsing|parsing|
|n-grams|n-gram|
|10Word inflection (pluralization and singularization) and lemmatization|inflection-lemmatization|
|Spelling correction|spelling-correction|

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
		"method": "method-key"
	}
}
```
