web: gunicorn Bank.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn Bank.wsgi