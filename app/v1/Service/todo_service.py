#PENDIENTE DE ELIMINCACION 

from fastapi import HTTPException, status

from app.v1.schema import todo_schema
from app.v1.schema import user_schema
from app.v1.Model.viaje_model import Resumen_viaje as Viaje


def create_task(task: todo_schema.TodoCreate, user: user_schema.User):

    db_task = Viaje(
        title=task.title,
        user_id=user.id
    )

    db_task.save()

    return todo_schema.Todo(
        id = db_task.id,
        title = db_task.title,
        is_done = db_task.is_done,
        created_at = db_task.created_at
    )