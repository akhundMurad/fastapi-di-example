from celery import Celery
from src.tasks_sender.base import TasksSender


class CeleryTasksSender(TasksSender):
    def __init__(self, celery: Celery) -> None:
        self.celery = celery

    def send_mail(self) -> None:
        self.celery.send_task("src.celery.app.send_mail")
