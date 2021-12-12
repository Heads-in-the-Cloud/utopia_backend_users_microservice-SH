# ######################################################################################################################
# ########################################                               ###############################################
# ########################################       SQLAlchemy Models       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_sqlalchemy import SQLAlchemy

# Initializing the SQLAlchemy Database ORM
db = SQLAlchemy()

# ------------------------------------------------
#                   Models Tables
# ------------------------------------------------


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role_id.id"), nullable=False)
    given_name = db.Column(db.String, nullable=False)
    family_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)


class UserRole(db.Model):
    __tablename__ = "user_role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)


# ------------------------------------------------
#                   Association Tables
# ------------------------------------------------


booking_agent = db.Table(
    "booking_agent",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("agent_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


booking_user = db.Table(
    "booking_user",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


flight_booking = db.Table(
    "flight_booking",
    db.metadata,
    db.Column("flight_id", db.Integer, db.ForeignKey("flight.id"), primary_key=True),
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True)
)
