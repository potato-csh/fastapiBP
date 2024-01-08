from fastapi import APIRouter, Query, status, Path

from experiment.schemas import (
    ExperimentListParams,
    ExperimentDetailResponse,
    ExperimentCreate,
    ExperimentPagination,
)
from experiment.service import (
    get_experiment_list,
    get_experiment_detail,
    experiment_create,
)
from database import DbSession, CommonParams


router = APIRouter()


@router.get("/experiment/list", status_code=status.HTTP_200_OK, response_model=ExperimentPagination)
def experiment_list(exp_list_params: ExperimentListParams, commons: CommonParams):
    experiment_list = get_experiment_list(**exp_list_params, **commons)

    return experiment_list


@router.get("/experiment/{experiment_id}", response_model=ExperimentDetailResponse)
def experiment_detail(db_session: DbSession, experiment_id: str = Path()):
    experiment_detail = get_experiment_detail(session=db_session, experiment_id=experiment_id)

    return experiment_detail


@router.post("/experiment", response_model=ExperimentDetailResponse)
def create_experiment(db_session: DbSession, param: ExperimentCreate):
    experiment = experiment_create(session=db_session, param=param)

    return experiment.id
