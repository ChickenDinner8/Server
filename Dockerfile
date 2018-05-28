FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN sudo apt-get install libmysqlclient-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
