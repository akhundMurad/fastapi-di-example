from motor import motor_asyncio
from src.dao.products import ProductDAO


def provide_products_dao(database: motor_asyncio.AsyncIOMotorDatabase) -> ProductDAO:
    return ProductDAO(database=database)
