from sqlalchemy import create_engine
from sqlalchemy.orm import Session


mysql_url_fmt = "mysql+pymysql://root:password@localhost:3306/ab_test"

engine = create_engine(mysql_url_fmt)

db_session = Session(engine)
