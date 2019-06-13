# Simple Text Processing

**category:** `language-processing`

**job_type:** `simple-text-processing`

**powered_by:** `TextBlob` (MIT): [Repo](https://github.com/sloria/TextBlob)

Common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

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
		"text": "Example text"
	},
	"options": {
		"method": "method-key"
	}
}
```
