# syntax=docker/dockerfile:1

FROM python:3.9-alpine

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password image_user
USER image_user

EXPOSE 8080/tcp

ENTRYPOINT ["python", "main.py"]

