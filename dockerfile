FROM python:3.9-alpine

ENV FLASK_APP project
ENV FLASK_CONFIG docker

WORKDIR /project

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY project project
COPY managerisk.py config.py boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]