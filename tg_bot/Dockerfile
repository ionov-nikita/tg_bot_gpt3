FROM python:3.11-slim-buster

RUN useradd magic

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY bot.py .
COPY common ./common
COPY src ./src

USER magic