release: python manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn BairBudalite_test1.wsgi --log-file -
