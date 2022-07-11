from typing import Callable

from celery import Celery
from src.celery.tasks import send_mail
from src.di.providers.celery import provide_celery
from src.di.providers.config import provide_config
from src.di.providers.services import provide_mails_service


def build_app() -> Celery:
    config = provide_config()
    app = provide_celery(config.redis_connection_string)

    nodepends_send_mail = _inject_dependency_to_task(
        send_mail, service=provide_mails_service()
    )

    app.task(nodepends_send_mail)

    return app


def _inject_dependency_to_task(task: Callable, **depends) -> Callable:
    nodepends = lambda: task(**depends)
    nodepends.__name__ = task.__name__
    return nodepends


app = build_app()
