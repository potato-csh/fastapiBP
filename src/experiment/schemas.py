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


class ExperimentCreate(ExperimentBase):
    pass


class ExperimentUpdate(ExperimentBase):
    pass
