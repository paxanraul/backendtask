from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.permission import AccessRoleRule, BusinessElement


def check_permission(element_name: str, action: str, require_all: bool = False):

    def permission_checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ) -> User:
        
        element = db.query(BusinessElement).filter(
            BusinessElement.name == element_name
        ).first()

        if element is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Бизнес объекта '{element_name}' не найден"
            )
        
        rule = db.query(AccessRoleRule).filter(
            AccessRoleRule.role_id == current_user.role_id,
            AccessRoleRule.element_id == element.id
        ).first()

        if rule is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав"
            )

        if require_all:
            permission_field = f"{action}_all_permission"
        else:
            permission_field = f"{action}_permission"

        has_permission = getattr(rule, permission_field, False)

        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"У вас нет прав на действие '{action}'"
            )
        
        return current_user
    
    return permission_checker