from fastapi import APIRouter

from fast_api_todo.schemas import TaskPublic, TaskSchema

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/tasks', response_model=TaskPublic)
def create_task(task: TaskSchema): ...
