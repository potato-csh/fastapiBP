import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException as StarletteHTTPException

from config import app_configs
from api import api_router
from models import Base
from database import engine


app = FastAPI(**app_configs)

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(api_router)


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(
#     request: Request,exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )


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
        log_level="info",
    )
