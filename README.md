Envio Web Backend Challenge
===========================

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker-Compose](https://docs.docker.com/compose/install/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Usage

    All the commands are needed to be run in the project root derictory

### Setup

    make install
    
Run it once to prepare the app to work
    
### Start

    make start
    
To run the app at `0.0.0.0:8888`

### Stop

    make stop
    
### Generate 10000 test DB records

    make generate-test-db-data

It can be run multiple times to add more devices

### Check deployment checklist

    make check-deploy
    
## Example of requests

### Send data

```shell script
curl --location --request POST 'http://0.0.0.0:8888/api/v1/reading' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "timestamp": "2022-01-29T00:00:00.111111+00:00",
        "reading": 1,
        "device_id": "ed8fb37b-6104-4009-8cda-85ad9bedb82f",
        "customer_id": "8c96b993-2a2f-4b40-a83a-7c705ba196c1"
    },
    {
        "timestamp": "2022-01-29T00:00:00.111111+00:00",
        "reading": 2,
        "device_id": "2c481695-0414-477c-8f00-abd22c679096",
        "customer_id": "8c96b993-2a2f-4b40-a83a-7c705ba196c1"
    },
    {
        "timestamp": "2022-01-29T00:01:00.111111+00:00",
        "reading": 1.5,
        "device_id": "ed8fb37b-6104-4009-8cda-85ad9bedb82f",
        "customer_id": "8c96b993-2a2f-4b40-a83a-7c705ba196c1"
    },
    {
        "timestamp": "2022-01-29T00:01:00.111111+00:00",
        "reading": 5.3,
        "device_id": "2c481695-0414-477c-8f00-abd22c679096",
        "customer_id": "8c96b993-2a2f-4b40-a83a-7c705ba196c1"
    }
]'
```

### Retrieve aggregated data

```shell script
curl --location --request GET 'http://0.0.0.0:8888/api/v1/reading/aggr?from=2022-01-29T00:00:00Z&to=2122-01-29T00:00:00Z&customer_id=8c96b993-2a2f-4b40-a83a-7c705ba196c1&aggr_size_min=10' | json_pp
```

Possible query parameters: `to`, `from`, `customer_id`, `device_id`, `aggr_size_min` 
