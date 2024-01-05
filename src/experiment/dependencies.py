from fastapi import Query, Depends
from typing import Annotated
from datetime import datetime

from experiment.models import ExperimentStatus


def experiment_list_param(
    name: str = Query(None),
    owner: int = Query(None),
    layer_name: str = Query(None),
    status: str = Query(None, enum=["PENDING", "RUNNING", "STOPPED", "DELETED"]),
):
    return {
        "name": name,
        "owner": owner,
        "layer_name": layer_name,
        "status": status,
    }


ExperimentListParameters = Annotated[
    dict[str, int | str], Depends(experiment_list_param)
]


def create_experiment_param(
    name: str = Query(),
    description: str = Query(None),
    sampling_type: int = Query(),
    sampling_rate: int = Query(),
    layer_name: str = Query(),
    testing_url: str = Query(),
    testing_type: int = Query(),
    white_list: str = Query(None),
    black_list: str = Query(None),
    start_time_preset: datetime = Query(),
    end_time_preset: datetime = Query(),
):
    return {
        "name": name,
        "description": description,
        "sampling_type": sampling_type,
        "sampling_rate": sampling_rate,
        "layer_name": layer_name,
        "testing_url": testing_url,
        "testing_type": testing_type,
        "white_list": white_list,
        "black_list": black_list,
        "start_time_preset": start_time_preset,
        "end_time_preset": end_time_preset,
    }


CreateExperimentParameters = Annotated[
    dict[str, int | str | datetime], Depends(create_experiment_param)
]
