import uuid
from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.order_repo import save, get_by_id, get_many


def product_create(dto) -> Product:
    # Проверка данных
    if not dto.get('name'):
        raise ValueError('Name is required')
    if not dto.get('price'):
        raise ValueError('Price is required')

    # Создание продукта
    product = Product(
        id=str(uuid.uuid4()),
        name=dto['name'],
        price=dto['price'],
    )
    save(product)

    return product


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)
