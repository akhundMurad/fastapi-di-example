from fastapi import FastAPI

from src.di.providers.celery import provide_celery, provide_task_sender
from src.di.providers.config import provide_config
from src.di.providers.dao import provide_products_dao
from src.di.providers.db import provide_db
from src.di.providers.services import (provide_products_service,
                                       provide_products_service_stub)
from src.routes import products


def build_app() -> FastAPI:
    app = FastAPI()

    setup_di(app)

    app.include_router(products.router)

    return app


def setup_di(app: FastAPI) -> None:
    config = provide_config()

    nodepends_provide_celery = lambda: provide_celery(
        redis_connection_string=config.redis_connection_string
    )
    nodepends_provide_mongo_db = lambda: provide_db(
        mongo_connection_string=config.mongo_connection_string
    )
    nodepends_provide_task_sender = lambda: provide_task_sender(
        celery=nodepends_provide_celery()
    )
    nodepends_prodive_products_dao = lambda: provide_products_dao(
        database=nodepends_provide_mongo_db()
    )
    nodepends_provide_products_service = lambda: provide_products_service(
        dao=nodepends_prodive_products_dao(),
        tasks_sender=nodepends_provide_task_sender(),
    )

    app.dependency_overrides[
        provide_products_service_stub
    ] = nodepends_provide_products_service


app = build_app()
