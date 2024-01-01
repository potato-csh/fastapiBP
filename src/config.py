from typing import Any
from starlette.config import Config


app_configs: dict[str, Any] = {
    "title": "ABconsole",
    "description": "Welcome to ABconsole's API documentation",
    "docs_url": "/docs",
    "redoc_url": "/redoc",
}

config = Config(".env")