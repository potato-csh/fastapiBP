from fastapi import APIRouter


router = APIRouter()


@router.get("/exp_list")
async def experiment_list():
    return {"test": "fastapi"}
