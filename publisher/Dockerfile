# IMAGE PULL
FROM python:3.10

# FILE MOVE
COPY ./src/ /publisher/src/
COPY ./requirements.txt /publisher/requirements.txt


# ENVIRONMENT SETUP
WORKDIR /publisher
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt


# ACTIONABLE
ENTRYPOINT /usr/local/bin/python ./src/app/main.py
 