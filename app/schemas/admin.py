from pydantic import BaseModel
from typing import Optional


class UserRoleUpdate(BaseModel):
    role_id: int


class PermissionUpdate(BaseModel):
    read_permission: Optional[bool] = None
    read_all_permission: Optional[bool] = None
    create_permission: Optional[bool] = None
    update_permission: Optional[bool] = None
    update_all_permission: Optional[bool] = None
    delete_permission: Optional[bool] = None
    delete_all_permission: Optional[bool] = None