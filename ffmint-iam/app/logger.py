# app/logger.py
import logging

from app.config import settings

LOG_LEVEL = settings.log_level.upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("ffmint")
