"""Enpoints Listed"""

from fastapi import APIRouter

# Import the health check router
from app.api.v1.endpoints import health

# Create the main API router for version 1
health_router = APIRouter()

# Include the health check router
# This will make the health endpoint available at /api/v1/health
health_router.include_router(health.router, tags=["Health"])

# You would typically include other routers here, e.g.:
# from app.api.v1.endpoints import users
# api_router.include_router(users.router, prefix="/users", tags=["users"])
