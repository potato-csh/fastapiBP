from fastapi import APIRouter, Request
from typing import List, Optional

from src.experiment.schemas import ExperimentList
from src.experiment.service import get_experiment_list
from database import db_session

router = APIRouter()

@router.get("/list", response_model=ExperimentList)
async def experiment_list():
    # name: Optional[str] = None,
    # owner: Optional[int] = 0,
    # status: Optional[str] = enumerate,
    # layer_name: Optional[str] = None
    experiment_list = get_experiment_list(db_session)
    
    # items = [experiment for experiment in experiment_list]
    
    # return ExperimentList(
    #     items=items,
    #     page=10,
    #     total=100,
    #     itemsPerPage=10
    # )


@router.get("/{experiment_id}")
async def experiment_detail(request: Request):
    pass
