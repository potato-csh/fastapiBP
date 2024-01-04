from datetime import datetime

from models import Pagination, ABTestBase


class ExperimentBase(ABTestBase):
    id: int
    experiment_id: str
    name: str | None
    layer_name: str
    sampling_rate: int
    owner: int
    status: int | None
    start_time_preset: datetime | None
    end_time_preset: datetime | None
    create_at: datetime | None
    update_at: datetime | None


class ExperimentPagination(Pagination):
    items: list[ExperimentBase] = []

class ExperimentDetail(ExperimentBase):
    description: str
    origin_url: str
    testing_url: str
    testing_type: int
    sampling_type: int
    start_time_real: datetime
    end_time_real: datetime
    white_list: str
    black_list: str
    starter: int
    ender: int
    hit_count: int
    hit_key_count: int
    hash_set: str

class ExperimentCreate(ExperimentBase):
    pass


class ExperimentUpdate(ExperimentBase):
    pass
