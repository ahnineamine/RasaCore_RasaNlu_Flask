FROM ubuntu:18.04

# Upgrade pip
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip
RUN pip3 install tornado


# Install rasa
RUN pip3 install --no-cache rasa_nlu
RUN pip3 install --no-cache rasa_core

# Install spacy
RUN pip install --default-timeout=100 spacy==2.1.9

# Spacy FR installation
RUN pip install https://github.com/explosion/spacy-models/releases/download/fr_core_news_md-2.1.0/fr_core_news_md-2.1.0.tar.gz && python3 -m spacy link fr_core_news_md fr

ENV LANG C.UTF-8
ENV FLASK_APP "app.py"

WORKDIR /app
COPY . /app

# Set Pythonpath
ENV PYTHONPATH="$PYTHONPATH:/app/backend"

# Install dependencies
RUN pip3 install -r requirements.txt

# Run main
EXPOSE 5005
#CMD [ "python3","app.py" ]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5005"]
