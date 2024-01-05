from datetime import datetime

from models import Pagination, ABTestBase


class ExperimentBase(ABTestBase):
    name: str
    layer_name: str
    sampling_rate: int
    owner: int
    start_time_preset: datetime | None  # require
    end_time_preset: datetime | None  # require


class ExperimentList(ExperimentBase):
    id: int
    experiment_id: str
    status: int  # require 默认是0
    create_at: datetime | None  # require
    update_at: datetime | None  # require


class ExperimentPagination(Pagination):
    items: list[ExperimentList] = []


class ExperimentDetail(ExperimentList):
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


class ExperimentCreate(ExperimentBase):
    description: str | None
    origin_url: str
    sampling_type: int
    testing_type: int
    testing_url: str
    white_list: str
    black_list: str


class ExperimentUpdate(ExperimentBase):
    pass
