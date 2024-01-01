from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from datetime import datetime

from database import engine

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, server_default=func.current_timestamp())
