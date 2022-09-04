
FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "config.wsgi"]

