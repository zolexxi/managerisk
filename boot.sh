#!/bin/sh
source venv/bin/activate
exec gunicorn --bind 0.0.0.0:5000 managerisk:app