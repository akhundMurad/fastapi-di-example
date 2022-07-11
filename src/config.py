from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_connection_string: str
    redis_connection_string: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
