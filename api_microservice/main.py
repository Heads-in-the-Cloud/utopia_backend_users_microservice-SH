# ######################################################################################################################
# ########################################                               ###############################################
# ########################################              Main             ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import (
    crud as c,
    models as m,
    schemas as s
)

m.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Database dependency to ensure each action happens on its own database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################          API Routes           ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


# ------------------------------------------------
#                       Users
# ------------------------------------------------


@app.post("/api/v2/users/", response_model=s.UserFull)
def create_user(user: s.User, db: Session = Depends(get_db)):
    db_user = c.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="This email has already been registered.")
    return c.create_user(db=db, user=user)


@app.get("/api/v2/users/", response_model=List[s.UserFull])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = c.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/api/v2/users/id={user_id}", response_model=s.UserFull)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = c.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.get("/api/v2/users/email={user_email}", response_model=s.UserFull)
def read_user_email(user_email: str, db: Session = Depends(get_db)):
    db_user = c.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.get("/api/v2/users/username={username}", response_model=s.UserFull)
def read_user_username(username: str, db : Session = Depends(get_db)):
    db_user = c.get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.get("/api/v2/users/role_id={role_id}", response_model=List[s.UserFull])
def read_user_role_group(role_id: int, db: Session = Depends(get_db)):
    db_users = c.get_users_with_role(db, role_id=role_id)
    if not db_users:    # In python, an empty list is treated as a boolean False, so triggers if db_users is empty
        raise HTTPException(status_code=404, detail="No users with that role.")
    return db_users


@app.get("/api/v2/users/id_list", response_model=List[int])
def read_user_ids(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_ids = c.get_users_ids(db, skip=skip, limit=limit)
    if not user_ids:    # In python, an empty list is treated as a boolean False, so triggers if user_ids is empty
        raise HTTPException(status_code=404, detail="No more users in database.")
    return user_ids


@app.get("/api/v2/users/auth/{username}", response_model=s.UserFull)
def read_user_auth(username: str, db: Session = Depends(get_db)):
    db_user = c.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="Incorrect credentials. Error no: 01.")
    return db_user


# ------------------------------------------------
#                      User Roles
# ------------------------------------------------


@app.post("/api/v2/user_roles/", response_model=s.UserRoleFull)
def create_user_role(role: s.UserRole, db: Session = Depends(get_db)):
    db_user_role = c.get_role_by_name(db, name=role.name)
    if db_user_role:
        raise HTTPException(status_code=404, detail=f"Role with that name already exists. [id={db_user_role.id}]")
    return c.create_role(db, role)


@app.get("/api/v2/user_roles/", response_model=List[s.UserRoleFull])
def read_user_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_roles = c.get_roles(db, skip=skip, limit=limit)
    if not user_roles:  # In python, an empty list is treated as a boolean False, so triggers if user_roles is empty
        raise HTTPException(status_code=404, detail="No more user roles found.")
    return user_roles


@app.get("/api/v2/user_roles/name={name}", response_model=s.UserRoleFull)
def read_user_role_by_name(name: str, db: Session = Depends(get_db)):
    user_role = c.get_role_by_name(db, name=name)
    if not user_role:
        raise HTTPException(status_code=404, detail="No user role with that name.")
    return user_role
