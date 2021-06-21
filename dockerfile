FROM python:3.8

ENV FLASK_APP project
ENV FLASK_CONFIG docker

WORKDIR /project

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . .
COPY boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]