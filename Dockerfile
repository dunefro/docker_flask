FROM python:3.8.2-alpine

WORKDIR /workspace

COPY . .

RUN pip3 install -r requirements.txt

