from motor import motor_asyncio


class ProductDAO:
    def __init__(self, database: motor_asyncio.AsyncIOMotorDatabase):
        self.collection: motor_asyncio.AsyncIOMotorCollection = database.products

    async def create(self, **data) -> None:
        await self.collection.insert_one(data)
