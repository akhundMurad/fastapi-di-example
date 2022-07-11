from fastapi import APIRouter, Depends
from src.di.providers.services import provide_products_service_stub

from src.dto.products import CreateProduct
from src.services.products import ProductService


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", status_code=201)
async def create_product(
    item: CreateProduct,
    service: ProductService = Depends(provide_products_service_stub)
) -> None:
    await service.create_product_and_send_mail(item)
