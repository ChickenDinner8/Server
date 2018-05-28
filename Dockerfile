FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps python3 python3-dev mariadb-dev jpeg-dev py3-pillow build-base \
    && apk add --virtual .runtime-deps mariadb-client-libs \
    && pip3 install -r requirements.txt \
    && apk del .build-deps
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
