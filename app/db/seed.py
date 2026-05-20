from sqlalchemy.orm import Session
from app.models.role import Role
from app.models.permission import BusinessElement, AccessRoleRule


def seed_roles(db: Session):
    roles = [
        {"id": 1, "name": "admin", "description": "Администратор"},
        {"id": 2, "name": "user", "description": "Пользователь"},
        {"id": 3, "name": "manager", "description": "Менеджер"},
        {"id": 4, "name": "guest", "description": "Гость"},
    ]
    
    for role_data in roles:
        exists = db.query(Role).filter(Role.id == role_data["id"]).first()
        if not exists:
            db.add(Role(**role_data))
    db.commit()


def seed_business_elements(db: Session):
    elements = [
        {"id": 1, "name": "users", "description": "Пользователи"},
        {"id": 2, "name": "products", "description": "Товары"},
        {"id": 3, "name": "orders", "description": "Заказы"},
        {"id": 4, "name": "access_rules", "description": "Правила доступа"}
    ]

    for element in elements:
        exists = db.query(BusinessElement).filter(
            BusinessElement.id == element["id"]
        ).first()
        if not exists:
            db.add(BusinessElement(**element))
    db.commit()


def seed_access_rules(db: Session):
    rules = [
        # ADMIN
        {"role_id": 1, "element_id": 1, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": True, "delete_all_permission": True},
        {"role_id": 1, "element_id": 2, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": True, "delete_all_permission": True},
        {"role_id": 1, "element_id": 3, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": True, "delete_all_permission": True},
        {"role_id": 1, "element_id": 4, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": True, "delete_all_permission": True},

        # USER 
        {"role_id": 2, "element_id": 1, "read_permission": True, "read_all_permission": False, "create_permission": False, "update_permission": True, "update_all_permission": False, "delete_permission": True, "delete_all_permission": False},
        {"role_id": 2, "element_id": 2, "read_permission": True, "read_all_permission": True, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
        {"role_id": 2, "element_id": 3, "read_permission": True, "read_all_permission": False, "create_permission": True, "update_permission": True, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 2, "element_id": 4, "read_permission": False, "read_all_permission": False, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},

        # MANAGER 
         {"role_id": 3, "element_id": 1, "read_permission": True, "read_all_permission": True, "create_permission": False, "update_permission": True, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 3, "element_id": 2, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": True, "delete_all_permission": False},
         {"role_id": 3, "element_id": 3, "read_permission": True, "read_all_permission": True, "create_permission": True, "update_permission": True, "update_all_permission": True, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 3, "element_id": 4, "read_permission": True, "read_all_permission": False, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},

          # GUEST 
         {"role_id": 4, "element_id": 1, "read_permission": False, "read_all_permission": False, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 4, "element_id": 2, "read_permission": True, "read_all_permission": True, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 4, "element_id": 3, "read_permission": False, "read_all_permission": False, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
         {"role_id": 4, "element_id": 4, "read_permission": False, "read_all_permission": False, "create_permission": False, "update_permission": False, "update_all_permission": False, "delete_permission": False, "delete_all_permission": False},
    ]
    for rule in rules:
        exists = db.query(AccessRoleRule).filter(
            AccessRoleRule.role_id == rule["role_id"],
            AccessRoleRule.element_id == rule["element_id"]
        ).first()
        if not exists:
            db.add(AccessRoleRule(**rule))
    db.commit()


def run_seed(db: Session):
    seed_roles(db)
    seed_business_elements(db)
    seed_access_rules(db)
    print("Тестовые данные добавлены")