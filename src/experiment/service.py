from sqlalchemy import select
from sqlalchemy.orm import Session

from experiment.models import Experiment
from experiment.schemas import ExperimentBase

def get_experiment_list(db_session: Session, page_num, page_size) -> list[ExperimentBase]:
    # 偏移数
    offset_num = page_size * (page_num - 1)
    stmt = select(Experiment).offset(offset_num).limit(page_size)

    experiment_list = db_session.execute(stmt)
    items: list[ExperimentBase] = []
    for experiment in experiment_list.scalars():
        items.append(experiment.to_dict())

    return items
