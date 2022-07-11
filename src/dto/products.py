from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    count: int
    category: str
