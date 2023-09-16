# IMAGE PULL
FROM python:3.10

# FILE MOVE
COPY ./src/ /webapp/src/
COPY ./requirements.txt /webapp/requirements.txt

# ENVIRONMENT SETUP
WORKDIR /webapp
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt


# ACTIONABLE
ENTRYPOINT /usr/local/bin/python ./src/app/main.py
 