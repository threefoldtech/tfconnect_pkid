FROM ubuntu:latest

RUN apt-get update && apt-get -y install pip curl cron libssl-dev openssl python3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY backup-cron /etc/cron.d/backup-cron
RUN chmod 0644 /etc/cron.d/backup-cron
RUN crontab /etc/cron.d/backup-cron
RUN touch /var/log/cron.log


RUN chmod +x /app/start.sh

RUN ls

CMD './start.sh'
