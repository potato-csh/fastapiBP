from fastapi import APIRouter, Request

from experiment.schemas import Experiments

router = APIRouter()


@router.get("/exp_list")
async def experiment_list(request: Request, experiments: Experiments):
    return experiments
