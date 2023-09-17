# Setup

To account for the requirements of this project (check: [Coding Problem](../coding_problem.md)) all the functionalities of this project are collected into a single docker-compose file which can be used to start-up or shut-down the systems with single commands.

## Prerequisites

To run this project to it's capabilities the following systems need to be installed first before starting up.

* Docker (check installation commands for Docker [here](https://docs.docker.com/engine/install/))
* Docker Compose(check installation instructions for Docker-Compose [here](https://docs.docker.com/compose/install/))
* Any browser of choice

## Startup

Once the Docker and Docker-compose is installed and ensured.
Clone the Repository at [github.com/WolfDev8675/Exalens-CC](https://github.com/WolfDev8675/Exalens-CC/archive/refs/heads/main.zip). This will download a zip file of the Project to your download location.

After the download is done follow the following steps

1. Unzip/Extract the file contents.
2. Open a terminal.
3. From the terminal navigate to the location of the extracted folder.
4. Here execute the command ```ls -l``` to list the folder structure.
You would see something like this

    ```bash
    ls -l 

    total 48
    -rw-r--r-- 1 kali kali 2640 Sep 15 08:34 coding_problem.md
    -rw-r--r-- 1 kali kali 1674 Sep 16 10:58 docker-compose.yaml
    drwxr-xr-x 3 kali kali 4096 Sep 17 01:31 docs
    -rw-r--r-- 1 kali kali 1070 Aug 27 13:44 LICENSE
    drwxr-xr-x 3 kali kali 4096 Sep 15 12:03 mongodb
    drwxr-xr-x 2 kali kali 4096 Aug 29 01:25 mosquitto
    drwxr-xr-x 3 kali kali 4096 Aug 30 14:10 publisher
    -rw-r--r-- 1 kali kali  594 Sep 16 23:21 README.md
    drwxr-xr-x 3 kali kali 4096 Sep 13 03:42 redis
    drwxr-xr-x 2 root root 4096 Sep 17 02:29 redis.conf
    drwxr-xr-x 3 kali kali 4096 Sep  9 10:59 subscriber
    drwxr-xr-x 3 kali kali 4096 Sep  9 10:59 webapp
    ```

5. If you are starting up for the first time run the command

    ```bash
    docker-compose up -d --build 
    ```

    otherwise a simple ```docker-compose up -d``` will work.
    This will startup the whole system and the suite of services implemented in the docker compose.
6. For confirming the systems are running execute the ```docker ps``` command in the terminal which will reveal a list of services similar to this.

    ```bash
    docker ps   
    CONTAINER ID   IMAGE                                       COMMAND                  CREATED          STATUS          PORTS                                           NAMES
    64e85d89169e   webapp_api_service                          "/bin/sh -c '/usr/lo…"   17 seconds ago   Up 15 seconds   0.0.0.0:9070->9070/tcp, :::9070->9070/tcp       exalens-cc_py_webapp_1
    355eb43e09bd   subscriber_service                          "/bin/sh -c '/usr/lo…"   17 seconds ago   Up 16 seconds                                                   exalens-cc_py_subscriber_1
    0f9f21997428   publisher_service                           "/bin/sh -c '/usr/lo…"   18 seconds ago   Up 16 seconds   0.0.0.0:9050->9050/tcp, :::9050->9050/tcp       exalens-cc_py_publisher_1
    23a409e23a1d   mosquitto_service                           "/bin/sh -c 'mosquit…"   19 seconds ago   Up 17 seconds   0.0.0.0:1883->1883/tcp, :::1883->1883/tcp       exalens-cc_mosquitto_broker_1
    e648d0597269   mongodb/mongodb-community-server:6.0-ubi8   "python3 /usr/local/…"   19 seconds ago   Up 17 seconds   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   exalens-cc_database_mongo_1
    d95743d94227   redis:latest                                "docker-entrypoint.s…"   19 seconds ago   Up 17 seconds   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp       exalens-cc_cache_redis_1
                                                                            
    ```

7. To check the data see the [API Documentation](./apidoc.md)
8. To shutdown the services execute the command ```docker-compose down```

---
Jump into:

* Previous: [Introduction](./intro.md)
* Next: [Architecture & Design](./design.md)

<br>&emsp;&emsp;[Table of Contents](./docs.md)</br>

---
&copy; [Bishal Biswas](mailto:b.biswas_94587@ieee.org)
