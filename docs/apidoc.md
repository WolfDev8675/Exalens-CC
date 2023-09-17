# API Documentation

Device Data Web Application API documentation. This API provides access to sensor data, allowing you to retrieve the latest data entries or data within a specified time range.

## Table of Contents

1. [Get Latest Sensor Data](#get-latest-sensor-data)
2. [Get Sensor Data Within a Time Range](#get-sensor-data-within-a-time-range)

---

## Get Latest Sensor Data

### Endpoint

**GET** `/api/sensor/latest`

### Description

This endpoint allows you to retrieve the latest 10 data entries for a specific sensor.

### Parameters

- `sensor_id` (query parameter) - The unique identifier of the sensor for which you want to retrieve data.

### Example

**Request:**

```http
GET /api/sensor/latest?sensor_id=sensHumid-0001
```

**Response:**

```json
{
  "data":[
        {
            "timestamp": "2023-09-16T14:57:25.0",
            "sensor_id": "sensHumid-0001",
            "value": 43.5
        },
        // ... (9 more entries)
    ]
}
```

### Notes

- The response contains an array of the latest 10 data entries.

---

## Get Sensor Data Within a Time Range

### Endpoint

**POST** `/api/sensor/data`

### Description

This endpoint allows you to retrieve sensor data within a specified time range.

### Request Body

```json
{
  "sensor_id": "sensHumid-0001",
  "start_time": "2023-09-16T14:48:20.0",
  "end_time": "2023-09-16T14:57:25.0"
}
```

- `sensor_id` (string, required) - The unique identifier of the sensor for which you want to retrieve data.
- `start_time` (string, required) - The start time of the time range in ISO8601 formatted datetime.
- `end_time` (string, required) - The end time of the time range in ISO8601 formatted datetime.

### Example

**Request:**

```http
POST /api/sensor/data
```

**Request Body:**

```json
{
  "sensor_id": "sensHumid-0001",
  "start_time": "2023-09-16T14:48:20.0",
  "end_time": "2023-09-16T14:57:25.0"
}
```

**Response:**

```json
{
  "data": [
        {
            "timestamp": "2023-09-16T14:48:20.0",
            "sensor_id": "sensHumid-0001",
            "value": 42.2
        },
        {
            "timestamp": "2023-09-16T14:49:15.0",
            "sensor_id": "sensHumid-0001",
            "value": 41.8
        },
        // ... (additional entries within the specified time range)
    ]
}
```

### Notes

- The response contains an array of sensor data entries within the specified time range.

---
Jump into:

* Previous: [Flow of Data](./dataflow.md)
* Next: [Challenges faced](./challenges.md)

<br>&emsp;&emsp;[Table of Contents](./docs.md)</br>

---
&copy; [Bishal Biswas](mailto:b.biswas_94587@ieee.org)
