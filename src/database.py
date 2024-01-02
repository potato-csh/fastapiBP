from typing import Dict, Any, List
from sqlalchemy import create_engine, Select, Insert, Update, CursorResult
from sqlalchemy.orm import Session


mysql_url_fmt = "mysql+pymysql://root:password@localhost:3306/ab_test"

engine = create_engine(mysql_url_fmt)

db_session = Session(engine)

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
