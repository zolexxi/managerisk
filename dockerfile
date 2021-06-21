FROM python:3.8

ENV FLASK_APP project
ENV FLASK_CONFIG docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY boot.sh .

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "project:create_app()"]