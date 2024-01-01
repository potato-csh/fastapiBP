from fastapi import APIRouter, Request
from typing import List, Optional

from database import db_session
from experiment.schemas import ExperimentList, ExperimentListResponse
from experiment.service import get_all

router = APIRouter()


@router.get("/list", response_model=List[ExperimentListResponse])
async def experiment_list(request: Request):
    # name: Optional[str] = None,
    # owner: Optional[int] = 0,
    # status: Optional[str] = enumerate,
    # layer_name: Optional[str] = None
    return get_all(db_session)

@router.get("/{experiment_id}")
async def experiment_detail(request: Request):
    pass
