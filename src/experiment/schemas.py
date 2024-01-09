from datetime import datetime
from fastapi import Query
from pydantic import Field
from uuid import UUID
from typing import Optional

from models import Pagination, ABTestBase, PrimaryKey


# Pydantic models


class ExperimentBase(ABTestBase):
    name: str
    layer_name: str
    sampling_rate: int = Field(10)
    start_time_preset: Optional[datetime] = Field(nullable=True)
    end_time_preset: Optional[datetime] = Field(nullable=True)


class ExperimentList(ExperimentBase):
    owner: int
    status: int = Field(0)
    id: PrimaryKey
    experiment_id: UUID
    created_at: datetime
    updated_at: datetime


class ExperimentCreate(ExperimentBase):
    origin_url: Optional[str] = Field(nullable=True)
    description: str = Field(None)
    sampling_type: int = Field(0)
    testing_type: int = Field(0)
    testing_url: str
    white_list: Optional[str] = Field(None, nullable=True)
    black_list: Optional[str] = Field(None, nullable=True)


class ExperimentRead(ExperimentList, ExperimentCreate):
    start_time_real: Optional[datetime] = Field(nullable=True)
    end_time_real: Optional[datetime] = Field(nullable=True)
    hit_count: Optional[int] = Field(0, nullable=True)
    hit_key_count: Optional[int] = Field(0, nullable=True)
    hash_set: Optional[str] = Field(None, nullable=True)


# class ExperimentUpdateResponse(ExperimentBaseResponse):
#     pass


class ExperimentPagination(Pagination):
    items: list[ExperimentList] = []
