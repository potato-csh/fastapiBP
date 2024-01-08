from datetime import datetime
from fastapi import Query
from pydantic import BaseModel, Field

from models import Pagination, ABTestBase


from fastapi import Query, Depends
from typing import Annotated

# Query

def experiment_list_parameters(
    name: str = Query(None),
    owner: int = Query(None),
    layer_name: str = Query(None),
    status: str = Query(None, enum=["PENDING", "RUNNING", "STOPPED", "DELETED"])
):
    return {
        "name": name,
        "owner": owner,
        "layer_name": layer_name,
        "status": status
    }


ExperimentListParams = Annotated[dict[str, int | str], Depends(experiment_list_parameters)]


class ExperimentCreate(ABTestBase):
    name: str = Field()
    description: str = Field(None)
    sampling_type: int = Field()
    sampling_rate: int = Field()
    layer_name: str = Field()
    testing_url: str = Field()
    testing_type: int = Field()
    white_list: str = Field(None)
    black_list: str = Field(None)
    start_time_preset: datetime = Field()
    end_time_preset: datetime = Field()


# Response...
    
class ExperimentBaseResponse(ABTestBase):
    name: str
    layer_name: str
    sampling_rate: int
    owner: int
    start_time_preset: datetime | None  # require
    end_time_preset: datetime | None  # require


class ExperimentListResponse(ExperimentBaseResponse):
    id: int
    experiment_id: str
    status: int  # require 默认是0
    create_at: datetime | None  # require
    update_at: datetime | None  # require


class ExperimentPagination(Pagination):
    items: list[ExperimentListResponse] = []


class ExperimentDetailResponse(ExperimentListResponse):
    description: str
    sampling_type: int
    origin_url: str
    testing_url: str
    testing_type: int
    start_time_real: datetime | None
    end_time_real: datetime | None
    white_list: str
    black_list: str
    hit_count: int
    hit_key_count: int
    hash_set: str


# class ExperimentCreateResponse(ExperimentBaseResponse):
#     description: str | None
#     origin_url: str
#     sampling_type: int
#     testing_type: int
#     testing_url: str
#     white_list: str
#     black_list: str


# class ExperimentUpdateResponse(ExperimentBaseResponse):
#     pass
