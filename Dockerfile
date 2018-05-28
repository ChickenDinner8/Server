FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps mariadb-dev \
    && pip install -r requirements.txt
    && apk add --virtual .runtime-deps mariadb-client-libs \
    && apk del .build-deps
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
