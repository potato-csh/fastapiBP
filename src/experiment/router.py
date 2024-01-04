from fastapi import APIRouter, Request, status
from experiment.dependencies import ExperimentQuery
from experiment.models import Experiment

from experiment.schemas import ExperimentPagination
from experiment.service import get_experiment_list
from database import CommonParameters


router = APIRouter()

@router.get("/list", status_code=status.HTTP_200_OK ,response_model=ExperimentPagination)
async def experiment_list(commons: CommonParameters, exp_query: ExperimentQuery):
    experiment_list = get_experiment_list(**commons, **exp_query)
    return experiment_list


@router.get("/{experiment_id}")
async def experiment_detail(request: Request):
    pass
