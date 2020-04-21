FROM python:3.8.2

RUN pip install pipenv

WORKDIR /app
COPY app .

RUN pipenv install --system

CMD ["python", "app.py"]