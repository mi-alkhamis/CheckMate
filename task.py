
from models import Task, task_schema
from flask import abort


def read_one(task_id):
    task = Task.query.filter(Task.id == task_id).one_or_none()
    if task is not None:
        return task_schema.dump(task)
    else:
        abort(
            404, f"The {task_id} does not exist."
        )