from typing import Any
from fastapi import APIRouter 
from core.celery_app import celery_app

router = APIRouter()

def celery_on_message(task, back_message):
    print(back_message)

def rate_task_get(task):
    return task.get(callback=celery_on_message, propagate=False)

@router.post("/", status_code=201)
async def rates_celery() -> Any:
    """
    Call Rates Celery worker.
    """
    task = celery_app.send_task("tasks.tasks.benchmark_rate", args=["hello"])
    result = task.get(propagate=False)
    print(result)
    return result
