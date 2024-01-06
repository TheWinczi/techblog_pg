#!/bin/bash

python manage.py makemigrations

if [ "${DEVELOPMENT}" = "true" ]; then
  python manage.py migrate &&
  python manage.py loaddata groups.json &&
  python manage.py loaddata accounts.json &&
  python manage.py loaddata posts.json &&
  python manage.py loaddata comments.json
else
    echo "Zmienna DEVELOPMENT (= ${DEVELOPMENT}) nie jest ustawiona na true. Nie zainicjalizowano danych."
fi

