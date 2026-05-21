from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.permissions import check_permission
from app.schemas.admin import UserRoleUpdate, PermissionUpdate
from app.schemas.user import UserResponse
from app.services.admin_service import (
    get_all_permissions,
    get_all_users,
    update_permission,
    update_user_role
)


router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users")
def list_user(
    current_user = Depends(check_permission("users", "read", require_all=True)),
    db: Session = Depends(get_db)
):
    return get_all_users(db)


@router.patch("/users/{user_id}/role")
def change_user_role(
    user_id: int,
    data: UserRoleUpdate,
    current_user = Depends(check_permission("users", "update", require_all=True)),
    db: Session = Depends(get_db)
):
    user = update_user_role(db, user_id, data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )
    return user


@router.get("/permissions")
def list_permissions(
    current_user = Depends(check_permission("access_rules", "read")),
    db: Session = Depends(get_db)
):
    return get_all_permissions(db)


@router.patch("/permissions/{rule_id}")
def edit_permission(
    rule_id: int,
    data: PermissionUpdate,
    current_user = Depends(check_permission("access_rules", "update")),
    db: Session = Depends(get_db)
):
    rule = update_permission(db, rule_id, data)
    if not rule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Правило не найдено"
        )
    return rule
    