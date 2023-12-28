from pydantic import BaseModel, Field
from typing import List, Optional
# from datetime import datetime


# class PydanticBase(BaseModel):
    

    # class Config:
    #     orm_mode = True
    #     arbitrary_types_allowed = True

"""
    id: int
    experiment_id: str = Field(max_length=40, unique=True)
    layer_name: str = Field(max_length=255)
    name: Optional[str] = Field(max_length=255)
    description: Optional[str] = Field(max_length=1024)
    origin_url: Optional[str] = Field(max_length=512)
    testing_url: Optional[str] = Field(max_length=512)
    testing_type: int = 0
    sampling_rate: int = 10
    sampling_type: int = 0
    start_time_preset: Optional[datetime]
    end_time_preset: Optional[datetime]
    start_time_real: Optional[datetime]
    end_time_real: Optional[datetime]
    update_time: Optional[datetime]
    status: Optional[int] = 0
    white_list: Optional[str] = Field(max_length=2048)
    black_list: Optional[str] = Field(max_length=2048)
    owner: int
    starter: int
    ender: int
    hit_count: Optional[int] = 0
    hit_key_count: Optional[int] = 0
    hash_set: Optional[str] = Field(max_length=512, default=None)
"""
class Experiments(BaseModel):
    name: Optional[str]
    owner: Optional[int]
    status: Optional[str]
    layer_name: Optional[str]
    
    pass

class ExperimentCreate(BaseModel):
    pass

class ExperimentUpdate(BaseModel):
    pass