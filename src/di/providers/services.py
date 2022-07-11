from src.tasks_sender.base import TasksSender
from src.dao.products import ProductDAO
from src.services.products import ProductService
from src.services.mails import MailsService


def provide_products_service_stub():
    ...


def provide_products_service(dao: ProductDAO, tasks_sender: TasksSender):
    return ProductService(dao=dao, tasks_sender=tasks_sender)


def provide_mails_service_stub():
    ...


def provide_mails_service() -> MailsService:
    return MailsService()
