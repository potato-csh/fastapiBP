from fastapi import APIRouter, Query, status, Path

from experiment.schemas import (
    ExperimentDetailResponse,
    ExperimentList,
    ExperimentCreate,
    ExperimentPaginationResponse,
)
from experiment.service import (
    get_experiment_list,
    get_experiment_detail,
    experiment_create,
)
from database import DbSession
from models import Commons


router = APIRouter()


@router.get(
    "/list",
    # status_code=status.HTTP_200_OK,
    # response_model=ExperimentPaginationResponse
)
def experiment_list(session: DbSession, commons: Commons, param: ExperimentList):
    experiment_list = get_experiment_list(session=session, **commons, **param)
    return experiment_list


@router.get("/{experiment_id}", response_model=ExperimentDetailResponse)
def experiment_detail(db_session: DbSession, experiment_id: str = Path()):
    experiment_detail = get_experiment_detail(
        session=db_session, experiment_id=experiment_id
    )
    return experiment_detail


@router.post("")
def create_experiment(db_session: DbSession, param: ExperimentCreate):
    experiment = experiment_create(session=db_session, param=param)

    return experiment.id
