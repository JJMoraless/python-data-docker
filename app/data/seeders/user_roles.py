from ...config.database import Session
from ..models.user_role import UserRoleModel


def seed_user_roles():
    session = Session()
    try:
        roles = ["ROOT", "ADMIN", "EMPLOYEE"]
        for role_name in roles:
            role = UserRoleModel(name_role=role_name)
            session.add(role)

        session.commit()
        print("Roles seeded successfully.")
    except Exception as e:
        print(f"Error seeding roles: REGISTROS DUPLICADOS")
        session.rollback()
    finally:
        session.close()
