from fastapi import APIRouter, Request
from typing import List, Optional

from experiment.schemas import ExperimentPagination
from experiment.service import get_experiment_list
from database import db_session

router = APIRouter()

@router.get("/list", response_model=ExperimentPagination)
async def experiment_list(
    page_num: Optional[int] = 1,
    page_size: Optional[int] = 1 
):
    # name: Optional[str] = None,
    # owner: Optional[int] = 0,
    # status: Optional[str] = enumerate,
    # layer_name: Optional[str] = None
    items = get_experiment_list(db_session, page_num, page_size)

    return ExperimentPagination(
        items=items,
        page=10,
        total=100,
        itemsPerPage=10
    )


@router.get("/{experiment_id}")
async def experiment_detail(request: Request):
    pass
