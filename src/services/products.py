from src.dao.products import ProductDAO
from src.dto.products import CreateProduct
from src.tasks_sender.base import TasksSender


class ProductService:
    def __init__(self, dao: ProductDAO, tasks_sender: TasksSender):
        self.dao = dao
        self.tasks_sender = tasks_sender

    async def create_product_and_send_mail(self, item: CreateProduct) -> None:
        await self.dao.create(**item.dict())

        self.tasks_sender.send_mail()
