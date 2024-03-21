from fastapi import APIRouter

from experiment.router import router as experiment_router


api_router = APIRouter(prefix="/api")

api_router.include_router(
    router=experiment_router, prefix="/experiment", tags=["experiment"]
)
