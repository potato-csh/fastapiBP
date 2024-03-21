from typing import Any, Dict
from starlette.config import Config


app_configs: Dict[str, Any] = {
    "title": "FastApiBP ABconsole",
    "description": "Welcome to ABconsole's API documentation",
    "version": "0.1.0",
    "openapi_url": "/api/openapi.json",
    "docs_url": "/api/docs",
    "redoc_url": "/redoc",
}

config = Config(".env")
