from pydantic import BaseModel


class AccessRuleResponse(BaseModel):
    id: int
    role_id: int
    element_id: int
    read_permission: bool
    read_all_permission: bool
    create_permission: bool
    update_permission: bool
    update_all_permission: bool
    delete_permission: bool
    delete_all_permission: bool

    model_config = {"from_attributes": True}  


class AccessRuleUpdate(BaseModel):
    read_permission: bool | None = None
    read_all_permission: bool | None = None
    create_permission: bool | None = None
    update_permission: bool | None = None
    update_all_permission: bool | None = None
    delete_permission: bool | None = None
    delete_all_permission: bool | None = None