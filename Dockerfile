FROM python:3.8.2-alpine
WORKDIR /workspace
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 main.py


################################################################################
FROM python:3.8.2-alpine AS haproxy
WORKDIR /workspace
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY haproxy.py .
CMD python3 haproxy.py