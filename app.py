from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

"""
Simple FastAPI backend for the AquaSync MVP prototype.

This backend exposes a handful of read‑only endpoints that return
dummy sensor data and descriptive information about the AquaSync
project. The endpoints are intentionally minimal so you can plug
them directly into a TypeScript/React frontend without having to
set up a database or authentication.  To run this API locally you
should first install the dependencies from ``requirements.txt`` and
then start the server with:

    uvicorn app:app --reload --host 0.0.0.0 --port 8000

The CORS middleware is configured to allow requests from any origin,
making it straightforward to develop the frontend in a separate
environment (e.g. Vite) without additional proxy configuration.
"""

# Instantiate the FastAPI application
app = FastAPI(title="AquaSync API", description="API serving dummy sensor data for the AquaSync MVP", version="0.1.0")

# Configure CORS to allow requests from frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aquasyncnodeweb-p2iht4um4-personal-d7db0365.vercel.app",
        "https://*.vercel.app",  # Allow all Vercel preview deployments
        "https://*.shreyasrk.com" # Allow all shreyasrk.com deployments
        "http://localhost:3000",  # Local development
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/api/info")
async def get_info() -> dict:
    """Return basic descriptive information about the AquaSync project.

    This endpoint delivers a summary of the mission, problem, solution and
    business model derived from the AquaSync pitch deck. It's useful
    for populating informational sections of the frontend without
    hardcoding text there.
    """
    return {
        "mission": "Secure India’s water future by transforming treatment plants from reactive to predictive.",
        "context": "India accounts for 18% of the global population but only 4% of fresh water. Per‑capita availability has been falling sharply since 1947 and is projected to drop another 47% by 2050. Decentralised sewage treatment plants operate inefficiently, reactively and with little transparency.",
        "problem": {
            "owners": "Plant owners suffer high costs from emergency repairs, wasted energy and long downtime because maintenance is reactive rather than preventative.",
            "vendors": "Service vendors operate on razor‑thin margins because their work is unplanned, they lack inventory visibility and they often need to make multiple site visits before diagnosing issues."
        },
        "solution": {
            "modules": "Easy to install IoT modules capture vibration, flow, pressure, energy and quality metrics from existing equipment.",
            "ai": "Machine learning models detect anomalies, predict failure, diagnose root causes and recommend actions.",
            "dashboard": "An intuitive dashboard delivers live insights, predictive alerts and auto‑generated work orders. A digital twin turns assets red when they’re about to fail.",
        },
        "business_model": "Sell the AquaSync box once, charge a recurring subscription for analytics and expand into a marketplace for parts and services."
    }


@app.get("/api/energy")
async def get_energy() -> dict:
    """Return dummy energy consumption data.

    The data returned represents monthly power usage in kilowatt hours (kWh)
    for a single treatment plant over the course of one year. This endpoint
    could be extended to accept query parameters identifying different
    plants or time ranges.
    """
    labels = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    data = [
        1500, 1425, 1470, 1600, 1550, 1580,
        1620, 1650, 1590, 1480, 1450, 1520
    ]
    return {"labels": labels, "data": data, "unit": "kWh"}


@app.get("/api/quality")
async def get_quality() -> dict:
    """Return dummy water quality data.

    The data models average weekly pH levels over a twelve‑week period.
    In a real deployment these values could represent turbidity, TDS or
    other key quality metrics.
    """
    labels = [f"Week {i}" for i in range(1, 13)]
    data = [
        7.1, 6.9, 7.0, 7.2, 7.1, 6.8,
        6.9, 7.0, 7.2, 7.3, 7.1, 6.9
    ]
    return {"labels": labels, "data": data, "unit": "pH"}


@app.get("/api/status")
async def get_status() -> dict:
    """Return dummy asset status distribution.

    This endpoint returns a breakdown of asset health statuses that can be
    visualised as a doughnut or pie chart. The numbers sum to 100 and
    represent the percentage of assets in each state.
    """
    labels = ["Operational", "Maintenance Needed", "Downtime"]
    data = [70, 20, 10]
    return {"labels": labels, "data": data}