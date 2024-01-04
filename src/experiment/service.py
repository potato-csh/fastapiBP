from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from experiment.models import Experiment, ExperimentStatus
from experiment.schemas import ExperimentBase


def get_experiment_filter(name, owner, layer_name, status):
    # 过滤条件拼接
    filters = []
    if status:
        try:
            status_code = ExperimentStatus[status]
            filters.append(Experiment.status == status_code.value)
        except KeyError:
            raise ValueError("Invalid status value")
    else:
        filters.append(Experiment.status != ExperimentStatus.DELETED.value)
    if name:
        filters.append(Experiment.name.contains(name))
    if owner:
        filters.append(Experiment.owner == owner)
    if layer_name:
        filters.append(Experiment.layer_name == layer_name)

    return filters


# def get_experiment_list(db_session: Session, page_num, page_size,
#                         name, owner, layer_name, status) -> list[ExperimentBase]:
#     # 偏移数
#     offset_num = page_size * (page_num - 1)

#     stmt = select(Experiment).where(and_(*filters)).offset(offset_num).limit(page_size)

#     experiment_list = db_session.execute(stmt)
#     items: list[ExperimentBase] = []
#     for experiment in experiment_list.scalars():
#         items.append(experiment.to_dict())

#     return items
