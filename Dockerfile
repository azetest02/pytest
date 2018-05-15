FROM python:3.6-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /app

ADD . /app

EXPOSE 5000

ENV FLASK_APP app.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]

