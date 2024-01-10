import enum
from uuid import UUID
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from experiment.schemas import ExperimentList, ExperimentRead

from models import Base


class ExperimentStatus(enum.IntEnum):
    PENDING = 0
    RUNNING = 1
    STOPPED = 2
    DELETED = 3


class Experiment(Base):
    __tablename__ = "experiment"

    owner: Mapped[int]
    starter: Mapped[int] = mapped_column(nullable=True)
    ender: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[int] = mapped_column(default=0)
    experiment_id: Mapped[UUID] = mapped_column(String(40))
    layer_name: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    origin_url: Mapped[str] = mapped_column(String(512), nullable=True)
    sampling_type: Mapped[int] = mapped_column(default=0)
    sampling_rate: Mapped[int] = mapped_column(default=10)
    testing_type: Mapped[int] = mapped_column(default=0)
    testing_url: Mapped[str] = mapped_column(String(512))
    white_list: Mapped[str] = mapped_column(String(2048), nullable=True)
    black_list: Mapped[str] = mapped_column(String(2048), nullable=True)
    start_time_preset: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time_preset: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    start_time_real: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time_real: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    hit_count: Mapped[int] = mapped_column(nullable=True, default=0)
    hit_key_count: Mapped[int] = mapped_column(nullable=True, default=0)
    hash_set: Mapped[str] = mapped_column(String(2048), default=None, nullable=True)
