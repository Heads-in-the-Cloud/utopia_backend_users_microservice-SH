# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        CRUD Operations        ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from . import (
    models as m,
    schemas as s
)

# ------------------------------------------------
#                       Users
# ------------------------------------------------


def get_user(db: Session, user_id: int):
    return db.query(m.User).filter(m.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(m.User).filter(m.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(m.User).filter(m.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.User).offset(skip).limit(limit).all()


def get_users_with_role(db: Session, role_id: int):
    return db.query(m.User).filter(m.User.role_id == role_id).all()


def get_users_ids(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(m.User).offset(skip).limit(limit).all()
    return [user.id for user in users]


def create_user(db: Session, user: s.User):
    hashed_password = generate_password_hash(user.password)
    db_user = m.User(
        role_id=user.role_id,
        given_name=user.given_name,
        family_name=user.family_name,
        username=user.username,
        password=hashed_password,
        email=user.email,
        phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ------------------------------------------------
#                      User Roles
# ------------------------------------------------


def get_role_by_name(db: Session, name: str):
    return db.query(m.UserRole).filter(m.UserRole.name == name).first()


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.UserRole).offset(skip).limit(limit).all()


def create_role(db: Session, role: s.UserRole):
    db_user_role = m.UserRole(name=role.name)

    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role