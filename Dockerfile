FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /mircroservice
COPY requirements.txt /mircroservice/requirements.txt
RUN pip install -r requirements.txt
COPY . /mircroservice/
