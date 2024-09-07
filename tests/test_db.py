from sqlalchemy import create_engine

from fast_api_todo.models import table_registry


def test_create_task():
    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)
