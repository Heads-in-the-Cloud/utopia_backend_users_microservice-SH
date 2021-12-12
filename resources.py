# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Restful Resources      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask import request
from flask_restful import Resource, Api

from schemas import *

# ------------------------------------------------
#                      User
# ------------------------------------------------


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)


class UserCreationResource(Resource):
    def post(self):
        new_user = User(
            role_id=request.json['role_id'],
            given_name=request.json['given_name'],
            family_name=request.json['family_name'],
            username=request.json['username'],
            password=request.json['password'],
            email=request.json['email'],
            phone=request.json['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserPatchResource(Resource):
    def patch(self, user_id):
        user = User.query.get_or_404(user_id)

        if 'user_id' in request.json:
            user.id = request.json['user_id']
        if 'role_id' in request.json:
            user.role_id = request.json['role_id']
        if 'given_name' in request.json:
            user.given_name = request.json['given_name']
        if 'family_name' in request.json:
            user.family_name = request.json['family_name']
        if 'username' in request.json:
            user.USERNAME = request.json['username']
        if 'password' in request.json:
            user.PASSWORD = request.json['password']
        if 'email' in request.json:
            user.email = request.json['email']
        if 'phone' in request.json:
            user.phone = request.json['phone']

        db.session.commit()
        return user_schema.dump(user)


class UserDeleteResource(Resource):
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                      UserRole
# ------------------------------------------------


class UserRoleResource(Resource):
    def get(self, role_id):
        user_role = UserRole.query.get_or_404(role_id)
        return user_role_schema.dump(user_role)


class UserRoleListResource(Resource):
    def get(self):
        user_roles = UserRole.query.all()
        return user_roles_schema.dump(user_roles)


class UserRoleCreationResource(Resource):
    def post(self):
        new_user_role = UserRole(
            name=request.json['name']
        )
        db.session.add(new_user_role)
        db.session.commit()
        return user_role_schema.dump(new_user_role)


class UserRolePatchResource(Resource):
    def patch(self, role_id):
        user_role = UserRole.query.get_or_404(role_id)

        if 'role_id' in request.json:
            user_role.id = request.json['role_id']
        if 'name' in request.json:
            user_role.name = request.json['name']

        db.session.commit()
        return user_role_schema.dump(user_role)


class UserRoleDeleteResource(Resource):
    def delete(self, role_id):
        user_role = UserRole.query.get_or_404(role_id)

        db.session.delete(user_role)
        db.session.commit()
        return '', 204


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################         Restful Routes        ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

api = Api()

# ------------------------------------------------
#                      User
# ------------------------------------------------

api.add_resource(UserResource, '/api/user/<user_id>')
api.add_resource(UserListResource, '/api/user/all')
api.add_resource(UserCreationResource, '/api/user/create')
api.add_resource(UserPatchResource, '/api/user/update/<user_id>')
api.add_resource(UserDeleteResource, '/api/user/delete/<user_id>')

# ------------------------------------------------
#                      UserRole
# ------------------------------------------------

api.add_resource(UserRoleResource, '/api/user_role/<role_id>')
api.add_resource(UserRoleListResource, '/api/user_role/all')
api.add_resource(UserRoleCreationResource, '/api/user_role/create')
api.add_resource(UserRolePatchResource, '/api/user_role/update/<role_id>')
api.add_resource(UserRoleDeleteResource, '/api/user_role/delete/<role_id>')