from fastapi import FastAPI

from fast_api_todo.routers import tasks

app = FastAPI()

app.include_router(tasks.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
