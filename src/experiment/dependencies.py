from fastapi import HTTPException, Query

from experiment.models import ExperimentStatus


# def validate_status(status: ExperimentStatus = Query(None, enum=["PENDING", "RUNNING", "STOPPED", "DELETED"])) -> str:
#     if status is None:
#         return None
#     if status not in ExperimentStatus.__members__:
#         raise HTTPException(status_code=422)
#     return status
