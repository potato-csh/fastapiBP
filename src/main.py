import uvicorn
from fastapi import FastAPI

from config import app_configs
from api import api_router
from models import Base
from database import engine


app = FastAPI(**app_configs)

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(api_router)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=5000,
        reload=True,
    )
