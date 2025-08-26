# AquaSync Backend Service

FastAPI backend service for the AquaSync water treatment plant monitoring system.

## Features

- RESTful API endpoints for sensor data
- CORS-enabled for frontend integration
- Dummy data for MVP demonstration
- Easy deployment to cloud platforms

## API Endpoints

- `GET /api/info` - Project information and business model
- `GET /api/energy` - Energy consumption data
- `GET /api/quality` - Water quality metrics
- `GET /api/status` - Asset health status distribution

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Deployment

This service is configured for deployment on Vercel, Railway, or similar platforms.

## Environment

- Python 3.8+
- FastAPI
- Uvicorn ASGI server

