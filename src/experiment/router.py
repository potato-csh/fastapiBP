from fastapi import APIRouter, Request, Depends
from typing import List, Optional
from experiment.dependencies import ExperimentQuery
from experiment.models import Experiment

from experiment.schemas import ExperimentPagination
from experiment.service import get_experiment_filter
from database import CommonParameters, search_filter_sort_paginate

router = APIRouter()


@router.get("/list", response_model=ExperimentPagination)
async def experiment_list(commons: CommonParameters, exp_query: ExperimentQuery):
    filter_str = get_experiment_filter(**exp_query)
    items = search_filter_sort_paginate(
        model=Experiment, filter_str=filter_str, **commons
    )

    return ExperimentPagination(items=items, page=10, total=100, itemsPerPage=10)


@router.get("/{experiment_id}")
async def experiment_detail(request: Request):
    pass
