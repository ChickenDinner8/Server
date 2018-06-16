FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apk update \
    && apk add --no-cache --virtual .build-deps mariadb-dev build-base \
    && apk add jpeg-dev mariadb-client-libs uwsgi-python3\
    && pip3 install -r requirements.txt \
    && apk del .build-deps
CMD ["uwsgi", "--ini", " /etc/uwsgi/uwsgi.ini"]
