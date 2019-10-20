FROM python:alpine

COPY requirements.pip /tmp/requirements.pip
RUN pip install -r /tmp/requirements.pip
