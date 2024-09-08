from pydantic import BaseModel


class Message(BaseModel):
    message: str

class TaskSchema(BaseModel):
    title: str
    description: str | None = None
    completed: bool | None = False


class TaskComplete(BaseModel):
    completed: bool


class TaskPublic(TaskSchema):
    id: int


class TaskList(BaseModel):
    tasks: list[TaskPublic]


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = False