export PYTHONPATH=/code:$PYTHONPATH

gunicorn schoolconfig.wsgi:application --bind :8001 --workers 4 
