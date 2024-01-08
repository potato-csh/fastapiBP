from datetime import datetime
from fastapi import Query
from pydantic import BaseModel, Field

from models import PaginationResponse, ABTestBase


class ExperimentList(BaseModel):
    name: str = Field(None)
    owner: int = Field(None)
    layer_name: str = Field(None)
    status: str = Field(None, enum=["PENDING", "RUNNING", "STOPPED", "DELETED"])


class ExperimentCreate(ABTestBase):
    name: str = (Field(),)
    description: str = (Field(None),)
    sampling_type: int = (Field(),)
    sampling_rate: int = (Field(),)
    layer_name: str = (Field(),)
    testing_url: str = (Field(),)
    testing_type: int = (Field(),)
    white_list: str = (Field(None),)
    black_list: str = (Field(None),)
    start_time_preset: datetime = (Field(),)
    end_time_preset: datetime = Field()


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


class ExperimentPaginationResponse(PaginationResponse):
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


class ExperimentCreateResponse(ExperimentBaseResponse):
    description: str | None
    origin_url: str
    sampling_type: int
    testing_type: int
    testing_url: str
    white_list: str
    black_list: str


class ExperimentUpdateResponse(ExperimentBaseResponse):
    pass
