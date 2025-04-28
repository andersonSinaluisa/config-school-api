cd code && \
export PYTHONPATH=/code:$PYTHONPATH
# Esperar a que Celery esté listo antes de iniciar Gunicorn
gunicorn schoolconfig.wsgi:application --bind :8001 --workers 4 
