from celery import Celery
from src.tasks_sender.celery import CeleryTasksSender


def provide_celery(redis_connection_string: str) -> Celery:
    return Celery(main=__name__, broker=redis_connection_string)


def provide_task_sender(celery: Celery) -> CeleryTasksSender:
    return CeleryTasksSender(celery=celery)
