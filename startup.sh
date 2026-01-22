gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:application --bind 0.0.0.0:8000
