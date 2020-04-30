####################################################################################################
# Covid Dash base image
####################################################################################################
FROM python:3.8.2-slim-buster AS covid-dash-base

RUN pip install pipenv==2018.11.26

WORKDIR /app

COPY app/api ./api
COPY app/helpers ./helpers
COPY app/app.py .
COPY app/Pipfile .
COPY app/Pipfile.lock .

####################################################################################################
# Covid Dash development image for test and debug
####################################################################################################
FROM covid-dash-base as covid-dash-development

COPY app/tests .
RUN pipenv install --system --dev

CMD ["python", "app.py"]

####################################################################################################
# Covid Dash deployable image
####################################################################################################
FROM covid-dash-base as covid-dash-app
RUN pipenv install --system

# CMD ["gunicorn", "-w 3", "app:server"]
CMD ["python", "app.py"]