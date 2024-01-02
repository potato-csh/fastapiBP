from typing import List
from sqlalchemy import select

from experiment.models import Experiment
from experiment.schemas import ExperimentList
from src.database import db_session

def get_experiment_list(db_session) -> ExperimentList:
    stmt = select(Experiment)
    experiment_list = db_session.execute(stmt)
    for experiment in experiment_list.scalars():
        print(experiment.name)

    return ExperimentList(
        items = experiment_list,
        itemsPerPage = 10,
        total = 100,
        page =  10,
    )