FROM python:3.8.5
ADD . /marvelApi
WORKDIR /marvelApi
RUN pip install -r requirements.txt