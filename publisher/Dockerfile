# IMAGE PULL
FROM python

# FILE MOVE
COPY ./src/ /publisher/src/
COPY ./requirements.txt /publisher/requirements.txt

# ENVIRONMENT SETUP
WORKDIR /publisher
RUN pip3 install -r ./requirements.txt


# ACTIONABLE
ENTRYPOINT /usr/local/bin/python ./src/app/main.py
 