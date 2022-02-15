FROM python:3.9.10

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install