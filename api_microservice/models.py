# ######################################################################################################################
# ########################################                               ###############################################
# ########################################       SQLAlchemy Models       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    role_id = Column(Integer, ForeignKey("user_role.id"), nullable=False)
    given_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    phone = Column(String, nullable=True)


class UserRole(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
