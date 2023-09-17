# Coding Challenge questionaire

Complete problem statement for the Coding Challenge as in the Mail

## Challenge Overview

### Purpose

Simulate the behaviour of sensors, monitor their readings, and provide APIs to retrieve data based on specific criteria.

1. MQTT Broker Setup: Deploy a Mosquitto MQTT broker using Docker.
2. MQTT Publisher: Create a Python MQTT client to mimic multiple sensor readings, publishing to topics like sensors/temperature and sensors/humidity.
    Structure of the JSON payload

        { "sensor_id": "unique_sensor_id", "value": "<reading_value>", "timestamp": "ISO8601_formatted_date_time" }:
3. MQTT Subscriber: Construct a Python MQTT subscriber to store the received messages in a MongoDB collection.
4. Data Storage: Initiate a MongoDB instance using Docker and save the incoming MQTT messages.
5. In-Memory Data Management: Implement Redis using Docker to store the latest ten sensor readings.
6. FastAPI Endpoint: Design an API with the following endpoints:
    * An endpoint that allows users to fetch sensor readings by specifying a start and end range.
    * An endpoint to retrieve the last ten sensor readings for a specific sensor.
7. Docker Integration: Integrate all services using Docker Compose.

### Deliverables

* Repository: Host the entire codebase on GitHub.
* Docker Compose: Include a docker-compose.yml file that ensures easy system setup. This file should encompass services for the Python apps (MQTT publisher, subscriber, FastAPI application), Mosquitto, MongoDB, and Redis.

File: Your repository should feature a comprehensive file detailing the following:

    * Instructions for setting up and interacting with the system using the docker-compose command.
    * A detailed overview of each service is in the docker-compose.yml file.
    * Insight into the design choices you made and the rationale behind them.
    * A section discussing challenges encountered during the project's development and the solutions you implemented.

### Guidelines

    * Ensure your code is well-commented and adheres to industry standards.
    * If you happen to encounter any ambiguities, please make informed assumptions and document them.

### Timeline & Submission

&nbsp;&nbsp;&nbsp;&nbsp; While we understand the complexity and depth of the challenge, three weeks should be sufficient. So, we'd like to ask you to submit your solution by <b>September 18th</b>. Please share the GitHub link of your repository once you've completed the task.

### Support

If you have any technical questions or require clarification on the challenge, please make decisions based on your understanding.

---
&copy; [Bishal Biswas](mailto:b.biswas_94587@ieee.org)
