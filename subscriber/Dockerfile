# IMAGE PULL
FROM python:3.10

# FILE MOVE
COPY ./src/ /subscriber/src/
COPY ./requirements.txt /subscriber/requirements.txt

# ENVIRONMENT SETUP
WORKDIR /subscriber
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt


# ACTIONABLE
ENTRYPOINT /usr/local/bin/python ./src/app/main.py
 