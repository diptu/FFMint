from app.db.base import Base  # or wherever you defined Base
from app.models.user import User  # import all models to register with metadata

__all__ = ["Base", "User"]
