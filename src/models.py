from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from datetime import datetime
from pydantic import BaseModel

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=True, server_default=func.current_timestamp())
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        server_default=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
    )

class ABTestBase(BaseModel):
    class ConfigDict:
        from_attributes = True
        # validate_assignment = True
        # arbitrary_types_allowed = True
        # anystr_strip_whitespace = True

        # json_encoders = {
        #     # custom output conversion for datetime
        #     datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%SZ") if v else None,
        #     # SecretStr: lambda v: v.get_secret_value() if v else None,
        # }

class Pagination(ABTestBase):
    itemsPerPage: int
    page: int
    total: int