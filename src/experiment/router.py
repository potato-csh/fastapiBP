from fastapi import APIRouter, status, Path

from experiment.dependencies import ExperimentListParameters, CreateExperimentParameters
from experiment.schemas import ExperimentPagination, ExperimentDetail, ExperimentCreate
from experiment.service import get_experiment_list, get_experiment_detail
from database import CommonParameters, DbSession


router = APIRouter()


@router.get(
    "/list", status_code=status.HTTP_200_OK, response_model=ExperimentPagination
)
async def experiment_list(
    commons: CommonParameters, exp_list_param: ExperimentListParameters
):
    experiment_list = await get_experiment_list(**commons, **exp_list_param)
    return experiment_list


@router.get("/{experiment_id}", response_model=ExperimentDetail)
async def experiment_detail(db_session: DbSession, experiment_id: str = Path()):
    experiment_detail = await get_experiment_detail(
        db_session=db_session, experiment_id=experiment_id
    )
    return experiment_detail


@router.post(response_model=ExperimentCreate)
async def create_experiment(
    db_session: DbSession, create_exp_param: CreateExperimentParameters
):
    pass
