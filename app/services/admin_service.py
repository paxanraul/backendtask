from sqlalchemy.orm import Session
from app.models.user import User
from app.models.permission import AccessRoleRule
from app.schemas.admin import UserRoleUpdate, PermissionUpdate


def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()


def update_user_role(db: Session, user_id: int, data: UserRoleUpdate) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.role_id = data.role_id
    db.commit()
    db.refresh(user)
    return user


def get_all_permissions(db: Session) -> list[AccessRoleRule]:
    return db.query(AccessRoleRule).all()


def update_permission(db: Session, rule_id: int, data: PermissionUpdate) -> AccessRoleRule | None:
    rule = db.query(AccessRoleRule).filter(AccessRoleRule == rule_id).first()
    if not rule:
        return None
    update_data = data.model_dump(exclude_none=True)
    for field, value in update_data.items():
        setattr(rule, field, value)
    db.commit()
    db.refresh(rule)
    return rule
