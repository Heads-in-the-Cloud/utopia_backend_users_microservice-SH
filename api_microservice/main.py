# ######################################################################################################################
# ########################################                               ###############################################
# ########################################              Main             ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

from typing import List

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

from .database import engine
from . import (
    models as m,
    schemas as s
)

m.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################          API Routes           ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


@app.get("/health")
def health_check():
    return "Healthy"


# ------------------------------------------------
#                       Users
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/users/", response_model=s.UserFull)
def create_user(user: s.User):
    with Session(engine) as db:
        db_user = db                                \
            .query(m.User)                          \
            .filter(m.User.email == user.email)     \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

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


# --------------------   Read   ------------------


@app.get("/api/v2/users/{user_id}", response_model=s.UserFull)
def get_user(user_id: int):
    with Session(engine) as db:
        db_user = db                        \
            .query(m.User)                  \
            .filter(m.User.id == user_id)   \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return db_user


@app.get("/api/v2/users/email={user_email}", response_model=s.UserFull)
def get_user_by_email(user_email: str):
    with Session(engine) as db:
        db_user = db                                \
            .query(m.User)                          \
            .filter(m.User.email == user_email)     \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return db_user


@app.get("/api/v2/users/username={username}", response_model=s.UserFull)
def get_user_by_username(username: str):
    with Session(engine) as db:
        db_user = db                                \
            .query(m.User)                          \
            .filter(m.User.username == username)    \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return db_user


@app.get("/api/v2/users/", response_model=List[s.UserFull])
def get_users(skip: int = 0, limit: int = 100):
    with Session(engine) as db:
        users = db              \
            .query(m.User)      \
            .offset(skip)       \
            .limit(limit)       \
            .all()

        # In python, an empty list is treated as a boolean False, so triggers if users is empty
        if not users:
            raise HTTPException(
                status_code=404,
                detail="No users found."
            )

        return users


@app.get("/api/v2/users/role_id={role_id}", response_model=List[s.UserFull])
def get_users_by_role(role_id: int):
    with Session(engine) as db:
        db_users = db                               \
            .query(m.User)                          \
            .filter(m.User.role_id == role_id)      \
            .all()

        # In python, an empty list is treated as a boolean False, so triggers if db_users is empty
        if not db_users:
            raise HTTPException(
                status_code=404,
                detail="No users with that role."
            )

        return db_users


@app.get("/api/v2/users/id_list", response_model=List[int])
def get_user_ids(skip: int = 0, limit: int = 100):
    with Session(engine) as db:
        users = db                  \
            .query(m.User)          \
            .offset(skip)           \
            .limit(limit)           \
            .all()

        # In python, an empty list is treated as a boolean False, so triggers if user_ids is empty
        if not users:
            raise HTTPException(
                status_code=404,
                detail="No more users in database."
            )

        user_ids = [user.id for user in users]

        return user_ids


@app.get("/api/v2/users/{username}/auth", response_model=s.UserAuth)
def get_user_auth(username: str):
    with Session(engine) as db:
        db_user = db                                \
            .query(m.User)                          \
            .filter(m.User.username == username)    \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        return db_user


# --------------------  Update  ------------------


@app.patch("/api/v2/users/{user_id}", response_model=s.UserFull)
def update_user(user_id: int, user: s.UserUpdate):
    with Session(engine) as db:
        db_user = get_user(user_id)

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


# --------------------  Delete  ------------------


@app.delete("/api/v2/users/{user_id}")
def delete_airplane(user_id: int):
    with Session(engine) as db:
        db_user = db                        \
            .query(m.User)                  \
            .filter(m.User.id == user_id)   \
            .first()

        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )

        db.delete(db_user)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                      User Roles
# ------------------------------------------------

# --------------------  Create  ------------------

@app.post("/api/v2/user_roles/", response_model=s.UserRoleFull)
def create_user_role(role: s.UserRole):
    with Session(engine) as db:
        db_role = db                                \
            .query(m.UserRole)                      \
            .filter(m.UserRole.name == role.name)   \
            .first()

        if db_role:
            raise HTTPException(
                status_code=404,
                detail="User role with that name already exists."
            )

        new_role = m.UserRole(name=role.name)

        db.add(new_role)
        db.commit()
        db.refresh(new_role)

        return new_role


# --------------------   Read   ------------------


@app.get("/api/v2/user_roles/{role_id}", response_model=s.UserRoleFull)
def get_user_role(role_id: int):
    with Session(engine) as db:
        db_role = db                            \
            .query(m.UserRole)                  \
            .filter(m.UserRole.id == role_id)   \
            .first()

        if not db_role:
            raise HTTPException(
                status_code=404,
                detail="User role not found"
            )

        return db_role


@app.get("/api/v2/user_roles/", response_model=List[s.UserRoleFull])
def get_user_roles(skip: int = 0, limit: int = 100):
    with Session(engine) as db:
        user_roles = db             \
            .query(m.UserRole)      \
            .offset(skip)           \
            .limit(limit)           \
            .all()

        if not user_roles:
            raise HTTPException(
                status_code=404,
                detail="No more user roles found."
            )

        return user_roles


@app.get("/api/v2/user_roles/name={name}", response_model=s.UserRoleFull)
def get_user_role_by_name(name: str):
    with Session(engine) as db:
        db_role = db                            \
            .query(m.UserRole)                  \
            .filter(m.UserRole.name == name)   \
            .first()

        if not db_role:
            raise HTTPException(
                status_code=404,
                detail="No user role with that name."
            )

        return db_role


# --------------------  Update  ------------------

# --------------------  Delete  ------------------


@app.delete("/api/v2/user_roles/{role_id}")
def delete_user_role(role_id: int):
    with Session(engine) as db:
        db_role = db                            \
            .query(m.UserRole)                  \
            .filter(m.UserRole.id == role_id)   \
            .first()

        if not db_role:
            raise HTTPException(
                status_code=404,
                detail="User role not found"
            )

        db.delete(db_role)
        db.commit()

        return {'ok': True}
