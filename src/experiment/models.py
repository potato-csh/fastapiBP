from sqlalchemy import Column, String, SmallInteger, BigInteger, DateTime
from sqlalchemy.sql import func

from src.models import Base


class Experiment(Base):
    __tablename__ = "experiment"

    id = Column(BigInteger, index=True, primary_key=True)
    experiment_id = Column(String(40), unique=True)
    layer_name = Column(String(25))
    name = Column(String(255), nullable=True)
    description = Column(String(1024), nullable=True)
    origin_url = Column(String(512), nullable=True)
    testing_url = Column(String(512), nullable=True)
    testing_type = Column(SmallInteger, default=0)
    sampling_rate = Column(SmallInteger, default=10)
    sampling_type = Column(SmallInteger, default=0)
    start_time_preset = Column(DateTime, nullable=True)
    end_time_preset = Column(DateTime, nullable=True)
    start_time_real = Column(DateTime, nullable=True)
    end_time_real = Column(DateTime, nullable=True)
    update_time = Column(
        DateTime,
        nullable=True,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
    status = Column(SmallInteger, nullable=True, default=0)
    white_list = Column(String(2048), nullable=True)
    black_list = Column(String(2048), nullable=True)
    owner = Column(SmallInteger)
    starter = Column(SmallInteger)
    ender = Column(SmallInteger)
    hit_count = Column(BigInteger, nullable=True, default=0)
    hit_key_count = Column(BigInteger, nullable=True, default=0)
    hash_set = Column(String(2048), default=None)
