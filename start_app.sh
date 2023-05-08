#!/bin/sh
# install gunicorn with `sudo apt install gunicorn` if needed

export FLASK_APP=garage_app.py
gunicorn --bind 0.0.0.0:8080 wsgi:app
