#
#FROM python:3.11-slim
#
#WORKDIR /blog
#
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#
#COPY run.py run.py
#COPY wsgi.py wsgi.py
##COPY config.py config.py
#COPY migrations migrations
#COPY blog ./blog
#COPY . .
#
#EXPOSE 5000
#
#CMD ["python", "run.py"]

FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache --user -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]



