"""
Health check endpoint for the IAM service.

This module provides a simple API route to check whether the service
and its dependencies (e.g., the database) are reachable.
"""

from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

# You might want to import your database session for a more thorough health check
# from app.db.session import get_db

router = APIRouter()


@router.get("/health", response_class=JSONResponse, summary="Health Check")
async def health_check() -> JSONResponse:
    """
    Performs a health check on the application.

    This endpoint can be used by load balancers, Kubernetes, or other
    monitoring systems to check the availability of the application.

    Returns:
        JSONResponse: A dictionary with a "status" key, indicating if the
                      application is "healthy".
    """
    try:
        return JSONResponse(
            content={"status": "healthy"}, status_code=status.HTTP_200_OK
        )
    except Exception as e:
        # If any check fails, return an unhealthy status
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Service unhealthy: {e}",
        ) from e
