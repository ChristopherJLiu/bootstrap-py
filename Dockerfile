FROM python:3.7.6-buster

ENV SERVICE_NAME=bootstrap-py \
    SERVICE_DESC='Boostrap project for Python based services' \
    SERVICE_TAGS='local,local-test,bootstrap-py' \
    SERVICE_CHECK_ENDPOINT='/' \
    SERVICE_CHECK_INTERVAL=10s \
    SERVICE_CHECK_TIMEOUT=2s \
    SERVICE_WEATHERAPI_CONFIG='[{"type":"owm","owm_list":[{"domain": "https://api.openweathermap.org", "path":"/data/2.5/weather", "args":"?id=2267057&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613","key":"244df0cbb2bcae2bca2fbe929ae3a613", "unit":"metric"}]}]' \
    NODE_ENV=dev

RUN apt-get update \
  && apt-get install \
    bash wget curl \
    inotify-tools -y

RUN rm -rf /var/cache/apk/*
RUN mkdir /app
WORKDIR /app


RUN pip install certifi
RUN pip install requests
RUN rm -rf /root/.cache

COPY ./app /app
ADD ./app /app
