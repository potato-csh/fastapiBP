from fastapi import Query, Depends
from typing import Annotated

from experiment.models import ExperimentStatus


def experiment_query(
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


ExperimentQuery = Annotated[dict[str, int | str], Depends(experiment_query)]
