FROM python:3.9

WORKDIR /src
COPY requirements.txt .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", '0.0.0.0:8000' ]
