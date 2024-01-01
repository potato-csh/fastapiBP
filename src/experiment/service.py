from typing import List

from .models import Experiment


def get_all(*, db_session) -> List[Experiment]:
    return db_session.query(Experiment)