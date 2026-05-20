from fastapi import APIRouter, Depends
from app.dependencies.permissions import check_permission
from app.models.user import User

router = APIRouter(prefix="/mock", tags=["mock"])


MOCK_PRODUCTS = [
    {"id": 1, "name": "Ноутбук", "price": 100000, "owner_id": 1},
    {"id": 2, "name": "Телефон", "price": 70000, "owner_id": 2},
    {"id": 3, "name": "Планшет", "price": 65000, "owner_id": 1},
]

MOCK_ORDERS = [
    {"id": 1, "product_id": 1, "status": "pending", "owner_id": 1},
    {"id": 2, "product_id": 2, "status": "completed", "owner_id": 2},
]


@router.get("/products/my")
def get_my_products(
    current_user: User = Depends(check_permission("products", "read"))
):
    return [p for p in MOCK_PRODUCTS if p["owner_id"] == current_user.id]


@router.post("/products")
def create_product(
    current_user: User = Depends(check_permission("products", "create"))
):
    return {"detail": "Товар создан (mock)", "owner_id": current_user.id}


@router.get("/orders")
def get_orders(
    current_user: User = Depends(check_permission("orders", "read"))
):
    return [o for o in MOCK_ORDERS if o["owner_id"] == current_user.id]


@router.get("/orders/all")
def get_all_orders(
    current_user: User = Depends(check_permission("orders", "read", require_all=True))
):
    return MOCK_ORDERS