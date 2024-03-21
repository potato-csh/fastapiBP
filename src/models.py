from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from datetime import datetime
from pydantic import BaseModel, ConfigDict, conint


# pydantic type that limits the range of primary keys
PrimaryKey = conint(gt=0, lt=2147483647)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, sort_order=-999)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), sort_order=999
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
        sort_order=999,
    )


class ABTestBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Pagination(ABTestBase):
    itemsPerPage: int
    page: int
    total: int
