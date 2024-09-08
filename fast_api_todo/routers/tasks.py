from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fast_api_todo.database import get_session
from fast_api_todo.models import Task
from fast_api_todo.schemas import TaskPublic, TaskSchema

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
