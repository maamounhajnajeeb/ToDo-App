ARG PYTHON_VERSION=3.11.0
FROM python:${PYTHON_VERSION}-slim as base
LABEL maintainer="Maamoun Haj Najeeb <maamoun.haj.najeeb@gmail.com>"

# means Python will not try to write .pyc files which we
# also do not desire
ENV PYTHONDONTWRITEBYTECODE 1

# ensures our console output looks familiar and is not buffered
# by Docker, which we don’t want
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

# RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -r requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get install -y libpq-dev

# copy all project files
COPY . .

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

USER appuser

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c" , "python manage.py migrate && gunicorn --env DJANGO_SETTINGS_MODULE=core.settings -c python:core.config.gunicorn_config core.wsgi"]
