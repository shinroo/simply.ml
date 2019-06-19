FROM python:latest

COPY . /platform

WORKDIR /platform/plugins/time_series/historical_data_forecasting
RUN pip install -r requirements.txt

WORKDIR /platform/plugins/language_processing/language_understanding
RUN pip install -r requirements.txt
RUN python -m snips_nlu download en

WORKDIR /platform/plugins/language_processing/simple_text_processing
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

WORKDIR /platform
RUN pip install -r requirements.txt

RUN pip install gunicorn
EXPOSE 8080
CMD python3 server.py
