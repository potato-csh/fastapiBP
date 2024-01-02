from typing import List, Optional
from datetime import datetime

from models import Pagination, ABTestBase

class ExperimentBase(ABTestBase):
    id: int
    experiment_id: str
    name: str
    layer_name: str
    sampling_rate: int
    owner: int
    status: int
    start_time_preset: datetime
    end_time_preset: datetime
    create_time: datetime
    update_time: datetime

class ExperimentList(Pagination):
    items: List[ExperimentBase] = []

class ExperimentCreate(ExperimentBase):
    pass

class ExperimentUpdate(ExperimentBase):
    pass