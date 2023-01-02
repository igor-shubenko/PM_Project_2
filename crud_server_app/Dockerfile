# syntax=docker/dockerfile:1

FROM python:3.10.8-slim

RUN apt-get update && apt-get install libpq-dev -y

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password crud_server_user
RUN chown crud_server_user:crud_server_user -R /app/
USER crud_server_user

EXPOSE 80/tcp

ENV DATABASE_LINK=$DATABASE_LINK
ENV BUCKET_NAME=$BUCKET_NAME
ENV FILE_NAME=$FILE_NAME

ENTRYPOINT ["python", "main.py"]

