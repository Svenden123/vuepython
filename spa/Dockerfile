FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get install nodejs

COPY /cron/mailer-cron /etc/cron.d/mailer-cron
RUN chmod 0644 /etc/cron.d/mailer-cron
RUN service cron start

WORKDIR /app/frontVue
RUN npm i sass-loader node-sass --save-dev
RUN npm i vue-cookie
RUN npm i
RUN npm run build

WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
