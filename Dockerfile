FROM python:3.10-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN apk update && apk upgrade && \
    apk add python3-dev \
                          gcc \
                          g++ \
                          libc-dev \
                          libffi-dev \
                          unixodbc \
                          unixodbc-dev && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install python-dotenv && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = true ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        baseuser

ENV PATH="/py/bin:$PATH"

USER baseuser