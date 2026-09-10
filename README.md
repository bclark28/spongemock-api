# spongemock-api

A lightweight Flask API that turns text into randomly mixed-case “SpOnGeMoCk” text.

## Requirements

- Python 3.9 or later
- Docker (optional, for containerized execution)

## Run locally

Create and activate a virtual environment, install the dependencies, and start the server:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
python app.py
```

The API listens on `http://localhost:5000`.

## Run with Docker

Build the image and run the API on port 5000:

```bash
docker build -t spongemock-api .
docker run --rm -p 5000:5000 spongemock-api
```

The container runs as an unprivileged user under Gunicorn and exposes a health endpoint at `GET /health`.

## API

### `GET /spongemock`

Pass the text to transform in the required `text` query parameter:

```bash
curl --get 'http://localhost:5000/spongemock' \
  --data-urlencode "text=we're going to need you to come in on saturday"
```

Successful requests return HTTP `200` and a JSON response. Letter casing is random, so the exact `mockedText` value changes between requests.

```json
{
  "error": null,
  "mockedText": "wE'Re GoiNG To neEd YoU tO COmE in on sAtURdAy"
}
```

If `text` is omitted, the API returns HTTP `400`:

```json
{
  "error": "query is not valid",
  "mockedText": null
}
```

### `GET /health`

Returns HTTP `200` when the service is ready to receive requests:

```json
{
  "status": "ok"
}
```

## Development

Run the test suite with:

```bash
pytest
```
