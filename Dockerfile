FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN apt-get install -y libmysqlclient-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
