from fastapi import APIRouter, Query, status, Path

from experiment.schemas import (
    ExperimentPagination,
    ExperimentRead,
    ExperimentCreate,
)
from experiment.service import (
    get_all,
    get_by_expid,
    create,
)
from database import DbSession, CommonParams


router = APIRouter()


@router.get(
    "/experiment", status_code=status.HTTP_200_OK, response_model=ExperimentPagination
)
def get_experiments(
    commons: CommonParams,
    name: str = Query(None),
    owner: int = Query(None),
    layer_name: str = Query(None),
    status: str = Query(None, enum=["PENDING", "RUNNING", "STOPPED", "DELETED"]),
):
    experiment_list = get_all(
        name=name, owner=owner, layer_name=layer_name, status=status, **commons
    )

    return experiment_list


@router.get(
    "/experiment/{experiment_id}",
    status_code=status.HTTP_200_OK,
    response_model=ExperimentRead,
)
def get_experiment(db_session: DbSession, experiment_id: str = Path()):
    experiment_detail = get_by_expid(session=db_session, experiment_id=experiment_id)

    return experiment_detail


@router.post("/experiment", response_model=ExperimentRead)
def create_experiment(db_session: DbSession, exp_in: ExperimentCreate):
    experiment = create(session=db_session, exp_in=exp_in)

    return experiment
