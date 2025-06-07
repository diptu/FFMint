from fastapi import FastAPI

from app.api.v1 import health_router

# --- Application setup ---
# Initialize the FastAPI application
app = FastAPI(
    title="FFMint-ima",  # Replace with your actual application title
    description="A brief description of your application.",  # Optional description
    version="1.0.0",  # Optional version
    openapi_url="/api/openapi.json",  # Standard OpenAPI path
    docs_url="/api/docs",  # Standard Swagger UI path
    redoc_url="/api/redoc",  # Standard ReDoc path
)

# _______ Include Routers----------------
app.include_router(health_router, prefix="/api/v1")
