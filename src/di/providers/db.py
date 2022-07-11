from motor import motor_asyncio


def provide_db_stub():
    ...


def provide_db(mongo_connection_string: str) -> motor_asyncio.AsyncIOMotorDatabase:
    client = motor_asyncio.AsyncIOMotorClient(mongo_connection_string)
    return client.get_database("dev")
