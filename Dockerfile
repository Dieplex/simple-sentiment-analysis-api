FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache g++
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m dostoevsky download fasttext-social-network-model
RUN apk del build-deps