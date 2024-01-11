from uuid import UUID
from fastapi import APIRouter, Query, Path
from experiment.models import ExperimentStatus

from experiment.schemas import (
    ExperimentCreateOrUpdate,
    ExperimentPagination,
    ExperimentRead,
)
from database import DbSession, CommonParams
from experiment.service import get_all, get_by_exp_id, create, update, delete

router = APIRouter()


@router.get("", response_model=ExperimentPagination)
def get_experiments(
    commons: CommonParams,
    name: str = Query(None),
    owner: int = Query(None),
    layer_name: str = Query(None),
    status: ExperimentStatus = Query(None),
):
    experiment_list = get_all(
        name=name, owner=owner, layer_name=layer_name, status=status, **commons
    )
    return experiment_list


@router.get("/{experiment_id}", response_model=ExperimentRead)
def get_experiment(db_session: DbSession, experiment_id: UUID = Path()):
    experiment = get_by_exp_id(session=db_session, exp_id=experiment_id)
    return experiment


@router.post("", response_model=ExperimentRead)
def create_experiment(db_session: DbSession, exp_in: ExperimentCreateOrUpdate):
    experiment = create(session=db_session, exp_in=exp_in)
    return experiment


@router.put("/{experiment_id}", response_model=ExperimentRead)
def update_experiment(
    db_session: DbSession, experiment_id: UUID, exp_in: ExperimentCreateOrUpdate
):
    experiment = update(session=db_session, exp_id=experiment_id, exp_in=exp_in)
    return experiment


@router.delete("/{experiment_id}", response_model=None)
def delete_experiment(db_session: DbSession, experiment_id: UUID):
    delete(session=db_session, exp_id=experiment_id)
