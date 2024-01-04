from sqlalchemy import and_, create_engine, select
from sqlalchemy.orm import Session
from fastapi import Query, Request, Depends
from typing import Annotated


mysql_url_fmt = "mysql+pymysql://root:password@localhost:3306/ab_test"

engine = create_engine(mysql_url_fmt)


def get_db(request: Request):
    return request.state.db


DbSession = Annotated[Session, Depends(get_db)]


def common_parameters(
    db_session: DbSession,
    sort_by: str = Query("id"),
    page_num: int = Query(1, gt=0, lt=2147483647),
    page_size: int = Query(1, gt=-2, lt=2147483647),
):
    return {
        "db_session": db_session,
        "sort_by": sort_by,
        "page_num": page_num,
        "page_size": page_size,
    }


CommonParameters = Annotated[
    dict[str, int | str | DbSession], Depends(common_parameters)
]


# async def fetch_one(select_query: Select | Insert | Update) -> Dict[str,Any]:
#     async with engine.begin() as conn:
#         cursor: CursorResult = await conn.execute(select_query)
#         return cursor.first()._asdict() if cursor.rowcount > 0 else None

# async def fetch_all(select_query: Select | Insert | Update) -> List[Dict[str, Any]]:
#     async with engine.begin() as conn:
#         cursor: CursorResult = await conn.execute(select_query)
#         return [r._asdict() for r in cursor.all()]

# async def execute(select_query: Insert | Update) -> None:
#     async with engine.begin() as conn:
#         await conn.execute(select_query)
