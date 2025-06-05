from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def health() -> dict[str, str]:
    """
    Performs a health check of the API.

    This function is an endpoint accessible via a GET request to '/health'.
    It is designed to provide a simple status indication of the API's
    operational state.

    Returns
    -------
    dict
        A dictionary containing the status of the health check.
        Example: `{"status": "ok"}`

    Examples
    --------
    >>> import requests
    >>> response = requests.get("http://localhost:8000/health") # Assuming the API is running locally
    >>> response.json()
    {'status': 'ok'}
    """
    return {"status": "ok"}
