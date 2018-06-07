FROM python:3.6.1
MAINTAINER Bahnlink "admin@bahnlink.com"

RUN mkdir /clean
VOLUME ["/clean"]
WORKDIR /clean

RUN pip install -U pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

CMD ["python", "manage.py", "sleep"]
