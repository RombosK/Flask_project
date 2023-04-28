#FROM python:3.9.1-buster
FROM python:3.9.16-slim

WORKDIR /blog

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY run.py run.py
COPY wsgi.py wsgi.py
COPY dev_config.json dev_config.json
COPY blog ./blog

EXPOSE 5000

CMD ["python", "run.py"]



