# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Pydantic Schemas       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from typing import List, Optional

from pydantic import BaseModel


# ------------------------------------------------
#                       Users
# ------------------------------------------------


class User(BaseModel):
    role_id: int
    username: str
    email: str
    given_name: str
    family_name: str
    password: str
    phone: str


class UserUpdate(BaseModel):
    role_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None


class UserAuth(BaseModel):
    username: str
    email: str
    password: str


class UserFull(User):
    id: int

    class Config:
        orm_mode = True


# ------------------------------------------------
#                      User Roles
# ------------------------------------------------


class UserRole(BaseModel):
    name: str


class UserRoleUpdate(BaseModel):
    name: Optional[str] = None


class UserRoleFull(UserRole):
    id: int

    class Config:
        orm_mode = True
