FROM python:3.8-alpine

ENV FLASK_APP managerisk.py
ENV FLASK_CONFIG docker

RUN adduser -D flasky
USER flasky

WORKDIR /home/flasky

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY managerisk.py config.py boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]