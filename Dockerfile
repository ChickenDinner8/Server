FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps mariadb-dev build-base \
    && apk add --virtual .runtime-deps jpeg-dev mariadb-client-libs \
    && pip3 install -r requirements.txt \
    && apk del .build-deps
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
