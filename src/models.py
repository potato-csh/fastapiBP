from typing import Annotated
from fastapi import Depends, Query
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from database import DbSession


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(index=True, primary_key=True, sort_order=-999)
    create_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, server_default=func.current_timestamp(), sort_order=999
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
        sort_order=999,
    )


class ABTestBase(BaseModel):
    model_config = ConfigDict(from_attributes = True)


class Pagination(ABTestBase):
    itemsPerPage: int
    page: int
    total: int
    