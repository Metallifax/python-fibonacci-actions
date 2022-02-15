FROM python:3.9.10

ENV WORKON_HOME /root

ENV PIPENV_PIPFILE /Pipfile

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile