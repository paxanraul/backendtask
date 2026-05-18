from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped,  mapped_column, relationship

from app.db.base import Base


class BusinessElement(Base):
    __tablename__ = "business_element"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(String(200))

    access_rules: Mapped[list["AccessRoleRule"]] = relationship(back_populates="element")


class AccessRoleRule(Base):
    __tablename__ = "access_role_rule"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    element_id: Mapped[int] = mapped_column(ForeignKey("business_element.id"))

    read_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    read_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    create_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    update_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    update_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    delete_permission: Mapped[bool] = mapped_column(Boolean, default=False)
    delete_all_permission: Mapped[bool] = mapped_column(Boolean, default=False)

    role: Mapped["Role"] = relationship(back_populates="access_rules")
    element: Mapped["BusinessElement"] = relationship(back_populates="access_rules")