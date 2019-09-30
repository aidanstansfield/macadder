FROM python:3-slim

RUN apt-get update && apt-get install -y \
libsasl2-dev \
libldap2-dev \
libssl-dev \
gcc

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app