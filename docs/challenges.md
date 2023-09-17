# Challenges faced

While loooking back to progress and development of this project, we encountered a series of challenges and difficulties that tested our problem-solving skills and determination. This section provides an overview of the obstacles we confronted, along with the strategies and solutions we employed to overcome them. Our journey through these challenges has not only strengthened our capabilities but also enriched our project's development.

1. Redis & MongoDB Server's own docker file has a docker-entrypoint command.

    * Problem: This problem is quite definitive for building Dockerfile. Since the image pull exercises a docker-entrypoint command the dockerfile in which we are pulling the image couldn't be having a ENTRYPOINT command or any RUN command in such a case. The Image confuses on itself which is the starting point and in the end fails to startup successfully with all the required commands.
    * Solution: Run the MongoDB Server and Redis directly in the Docker compose and not going for creating a separate docker file for customized purposes.

2. Mosquitto PAHO MQTT Client - in subscriber mode is always in auto persist condition.

    * Problem: When writing the Subscriber, we tried to follow the same scenario as the Publisher but it was eventually found that paho-MQTT client's loop-forever functionality keeps alive the communication with the broker and adding a server only conflicts with the priority of the code and adds complexity which other wise is totally avoidable.
    * Solution: Branched code into services but kept the starting point of the function to be handled solely by the paho client.

3. Redis Key:List takes strings and MongoDB documents are fully functional JSON objects.

    * Problem: When pushing data into the Redis we push everything as String data but MongoDB formats everything to objects when passed as dictionary from python. Hence MongoDB preserves the data-type as well as data but for Redis it doesn't preserve the data-type.
    * Solution: Customized utility function to recognize in each of the Python entities (Publisher, Subscriber, WebApp) how the data is feed into the system and take relative actions accordingly to modify or view as per solution.

---
Jump into:

* Previous: [API Documentation](./apidoc.md)

<br>&emsp;&emsp;[Table of Contents](./docs.md)</br>

---
&copy; [Bishal Biswas](mailto:b.biswas_94587@ieee.org)
