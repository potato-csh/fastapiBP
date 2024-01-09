import uvicorn
from fastapi import FastAPI, Request
from sqlalchemy.orm import Session

from config import app_configs
from api import api_router
from models import Base
from database import engine


app = FastAPI(**app_configs)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(api_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        db_session = Session(engine)
        request.state.db = db_session
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        request.state.db.close()

    return response


Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=5000,
        reload=True,
    )
