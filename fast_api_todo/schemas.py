from pydantic import BaseModel


class TaskSchema(BaseModel):
    title: str
    description: str | None = None
    completed: bool | None = False


class TaskPublic(TaskSchema):
    id: int


class TaskList(BaseModel):
    tasks: list[TaskPublic]
