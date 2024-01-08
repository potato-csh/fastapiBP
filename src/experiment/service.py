from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from utils import calculate_offset
from experiment.models import Experiment, ExperimentStatus
from experiment.schemas import (
    ExperimentCreate,
    ExperimentList,
    ExperimentPaginationResponse,
    ExperimentDetailResponse,
)


# 获取实验列表
def get_experiment_list(
    session: Session,
    sort_by: str,
    page_num: int,
    page_size: int,
    name,
    owner,
    layer_name,
    status,
) -> ExperimentPaginationResponse:
    # 实验过滤条件
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

    stmt = (
        select(Experiment)
        .where(and_(*filters))
        .order_by(sort_by)
        .offset(calculate_offset(page_num, page_size))
        .limit(page_size)
    )

    items: list[ExperimentList] = []
    for item in session.scalars(stmt):
        items.append(item.to_dict())

    return ExperimentPaginationResponse(
        items=items, page=page_num, total=len(items), itemsPerPage=page_size
    )


# 获取实验详情
def get_experiment_detail(
    session: Session, experiment_id: str
) -> ExperimentDetailResponse:
    stmt = select(Experiment).where(Experiment.experiment_id == experiment_id)
    experiment_detail = session.scalars(stmt).one_or_none().to_full_dict()

    return ExperimentDetailResponse(**experiment_detail)


# 创建实验
def experiment_create(session: Session, param: ExperimentCreate):
    experiment = Experiment(
        experiment_id=param.experiment_id,
    )

    pass
