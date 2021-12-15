# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Marshmallow Schemas      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_marshmallow import Marshmallow

from models import *

# Initializing Marshmallow Serialization Handler
ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "role_id", "given_name", "family_name", "username", "password", "email", "phone")
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserRoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = UserRole


user_role_schema = UserRoleSchema()
user_roles_schema = UserRoleSchema(many=True)