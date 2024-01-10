from fastapi import HTTPException, status
from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from uuid import uuid4, UUID

from utils import calculate_offset
from experiment.models import Experiment, ExperimentStatus
from experiment.schemas import (
    ExperimentList,
    ExperimentPagination,
    ExperimentRead,
    ExperimentCreateOrUpdate,
)

# 获取实验列表
def get_all(
    session: Session,
    sort_by: str,
    page_num: int,
    page_size: int,
    name,
    owner,
    layer_name,
    status,
) -> ExperimentPagination:
    # 实验过滤条件
    filters = []
    if status:
        filters.append(Experiment.status == ExperimentStatus[status].value)
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
        items.append(item)

    return ExperimentPagination(
        items=items, page=page_num, total=len(items), itemsPerPage=page_size
    )


# 获取实验详情
def get_by_exp_id(session: Session, exp_id: UUID) -> ExperimentRead:
    stmt = select(Experiment).where(Experiment.experiment_id == str(exp_id))
    experiment = session.scalars(stmt).one_or_none()
    if not experiment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Item not exist")
    return experiment


# 创建实验
def create(session: Session, exp_in: ExperimentCreateOrUpdate) -> ExperimentRead:
    exp_id = uuid4()
    experiment = Experiment(
        experiment_id=exp_id,
        name=exp_in.name,
        description=exp_in.description,
        layer_name=exp_in.layer_name,
        testing_type=exp_in.testing_type,
        testing_url=exp_in.testing_url,
        sampling_rate=exp_in.sampling_rate,
        sampling_type=exp_in.sampling_type,
        white_list=exp_in.white_list if exp_in.white_list else None,  # 如果存在则存入
        black_list=exp_in.black_list if exp_in.black_list else None,  # 如果存在则存入
        owner=0,  # user
        start_time_preset=exp_in.start_time_preset,
        end_time_preset=exp_in.end_time_preset,
    )

    session.add(experiment)
    session.commit()

    return experiment


def update(
    session: Session, exp_id: UUID, exp_in: ExperimentCreateOrUpdate
) -> ExperimentRead:
    experiment = get_by_exp_id(session=session, exp_id=exp_id)

    if experiment:
        experiment.name = (exp_in.name,)
        experiment.description = (exp_in.description,)
        experiment.layer_name = (exp_in.layer_name,)
        experiment.testing_type = (exp_in.testing_type,)
        experiment.testing_url = (exp_in.testing_url,)
        experiment.sampling_rate = (exp_in.sampling_rate,)
        experiment.sampling_type = (exp_in.sampling_type,)
        experiment.white_list = (
            exp_in.white_list if exp_in.white_list else None,
        )  # 如果存在则存入
        experiment.black_list = (
            exp_in.black_list if exp_in.black_list else None,
        )  # 如果存在则存入
        experiment.start_time_preset = exp_in.start_time_preset
        experiment.end_time_preset = exp_in.end_time_preset

        session.commit()

    return experiment


def delete(session: Session, exp_id: UUID):
    experiment = get_by_exp_id(session=session, exp_id=exp_id)

    session.delete(experiment)
    session.commit()
