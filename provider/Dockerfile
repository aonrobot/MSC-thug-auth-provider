FROM python:3.7
MAINTAINER Auttawut Wiriyakreng

RUN apt-get update && \
    apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*
ADD . /usr/src/appProvider
WORKDIR /usr/src/appProvider
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn provider.wsgi:application --bind 0.0.0.0:8000 --workers 3