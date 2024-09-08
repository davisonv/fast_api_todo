from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_api_todo.database import get_session
from fast_api_todo.models import Task
from fast_api_todo.schemas import TaskPublic, TaskSchema, TaskComplete, TaskUpdate, TaskList, Message

router = APIRouter(prefix='/tasks', tags=['tasks'])

Session = Annotated[Session, Depends(get_session)]


@router.post('/', response_model=TaskPublic)
def create_task(task: TaskSchema, session: Session):
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.put('/{task_id}', response_model=TaskPublic)
def put_task(task_id: int, session: Session, task: TaskSchema):
    db_task = session.scalar(select(Task).where(Task.id == task_id))

    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.patch('/{task_id}', response_model=TaskUpdate)
def patch_task(task_id: int, session: Session, task: TaskComplete):
    db_task = session.scalar(select(Task).where(Task.id == task_id))

    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.get('/{task_id}', response_model=TaskPublic)
def get_task(task_id: int, session: Session):
    db_task = session.scalar(select(Task).where(Task.id == task_id))

    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )
    
    return db_task


@router.get('/', response_model=TaskList)
def list_tasks(session: Session):

    tasks = session.scalars(select(Task)).all()

    return {"tasks": tasks}


@router.delete('/{task_id}', response_model=None, status_code=204)
def delete_todo(task_id: int, session: Session):
    task = session.scalar(
        select(Task).where(Task.id == task_id)
    )

    if not task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    session.delete(task)
    session.commit()

    return 
