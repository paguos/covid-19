FROM python:3.8.2 AS base

RUN pip install pipenv

WORKDIR /app
COPY app .

FROM base as test
RUN pipenv install --system --dev

FROM base as app
RUN pipenv install --system
CMD ["python", "app.py"]