FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata groups.json
RUN python manage.py loaddata accounts.json
RUN python manage.py loaddata posts.json
RUN python manage.py loaddata comments.json
CMD python manage.py runserver 0.0.0.0:8000


