# PULL 
FROM eclipse-mosquitto

# FILE MOVE
COPY ./mosquitto.conf  /

# ENVIRONMENT -LOCAL
EXPOSE 1883

# ACTIONABLE
ENTRYPOINT mosquitto -v \
    -p 1883:1883 \
    -c ./mosquitto.conf
    