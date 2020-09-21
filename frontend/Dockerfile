
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y apt-transport-https && apt-get -y install curl gnupg && curl -sL https://deb.nodesource.com/setup_13.x  | bash - && apt-get -y install nodejs


WORKDIR /app/frontend
COPY . /app/frontend

RUN npm install 

VOLUME /app/frontend

CMD npm start