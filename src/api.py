from fastapi import APIRouter

from experiment.router import router as experiment_router


api_router = APIRouter()

api_router.include_router(experiment_router, prefix="/experiment", tags=["experiment"])
