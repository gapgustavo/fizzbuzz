# syntax=docker/dockerfile:1

FROM python:3.11.3

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]