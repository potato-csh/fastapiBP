from sqlalchemy import Column, String, SmallInteger, BigInteger, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.models import Base


class Experiment(Base):
    __tablename__ = "experiment"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    experiment_id: Mapped[str] = mapped_column(String(40), unique=True)
    layer_name: Mapped[str] = mapped_column(String(25))
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    origin_url: Mapped[str] = mapped_column(String(512), nullable=True)
    testing_url: Mapped[str] = mapped_column(String(512), nullable=True)
    testing_type: Mapped[int] = mapped_column(default=0)
    sampling_rate: Mapped[int] = mapped_column(default=10)
    sampling_type: Mapped[int] = mapped_column(default=0)
    start_time_preset: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time_preset: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    start_time_real: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    end_time_real: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    status: Mapped[int] = mapped_column(nullable=True, default=0)
    white_list: Mapped[str] = mapped_column(String(2048), nullable=True)
    black_list: Mapped[str] = mapped_column(String(2048), nullable=True)
    owner: Mapped[int]
    starter: Mapped[int]
    ender: Mapped[int]
    hit_count: Mapped[int] = mapped_column(nullable=True, default=0)
    hit_key_count: Mapped[int] = mapped_column(nullable=True, default=0)
    hash_set: Mapped[str] = mapped_column(String(2048), default=None)