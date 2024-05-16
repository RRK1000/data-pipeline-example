# storage-layer
The Storage layer is a FastAPI server that accepts filtered data from the processing-svc to then push it into a Postgres Database

## Environment Variable(s)
KAFKA_URL : Kafka Instance Endpoint (default: localhost:9094)

## Running the application
```
uvicorn app.main:app --host <HOST_URL> --port <HOST_PORT>
```