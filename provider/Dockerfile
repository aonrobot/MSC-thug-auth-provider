FROM python:3.7
ENV PYTHONUNBUFFERED 1
MAINTAINER Auttawut Wiriyakreng

# Python lib
########################################
RUN apt-get update && \
    apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install SQL Server Driver
######################################
# 1. install system util
RUN apt-get update && apt-get install -y curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-6 && \
    rm -rf /var/lib/apt/lists/*
# 2. Microsoft repo
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 3. SQL Driver
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# 4. necessary location
RUN apt-get update && apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
# 5. another tool
RUN apt-get update && apt-get install gettext nano vim -y && \
    rm -rf /var/lib/apt/lists/*


#ADD . /usr/src/appProvider
WORKDIR /usr/src/appProvider
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

#CMD exec gunicorn provider.wsgi:application --bind 0.0.0.0:8000 --workers 3 --reload
#CMD exec python3 manage.py runserver