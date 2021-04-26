#!/bin/sh
source venv/bin/activate
flask deploy
exec gunicorn --bind 0.0.0.0:5000 managerisk:app