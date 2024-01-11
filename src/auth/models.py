from models import Base
from sqlalchemy.orm import mapped_column, Mapped


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=True)


class Role(Base):
    __tablename__ = "user"
