
FROM python:3.8-alpine

COPY . /app

# Устанавливаем все зависимости
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir

ENV FLASK_APP=main.py

EXPOSE 5000

CMD  flask run
