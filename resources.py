# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Restful Resources      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask import request, jsonify, make_response
from flask_restful import Resource, Api

from schemas import *

# ------------------------------------------------
#                      User
# ------------------------------------------------


class UserResource(Resource):
    def post(self):
        user = None

        if 'user_id' in request.json:
            user = User.query.filter_by(id=request.json['user_id']).first()
        elif 'email' in request.json:
            user = User.query.filter_by(email=request.json['email']).first()
        else:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'Neither user_id nor email provided. Please provide at least one.'
            }), 401)

        return user_schema.dump(user)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)


class UserNumberListResource(Resource):
    def get(self):
        users = User.query.all()
        user_nums = []
        for user in users:
            user_nums.append(user.id)
        return user_nums


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

        user = User.query.filter_by(email=new_user.email).first()

        if not user:
            db.session.add(new_user)
            db.session.commit()
            return make_response(jsonify(user_schema.dump(new_user)), 201)
        else:
            return make_response(jsonify({
                'status': 'failure',
                'message': 'User already exists for that email. Please log in.'
            }), 202)


class UserPatchResource(Resource):
    def post(self):
        user_id = request.json['user_id']
        user = User.query.get_or_404(user_id)

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
    def post(self):
        user_id = request.json['user_id']
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({
            'message': 'Successfully deleted.'
        }), 204)


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
    def post(self):
        role_id = request.json['role_id']
        user_role = UserRole.query.get_or_404(role_id)

        if 'role_id' in request.json:
            user_role.id = request.json['role_id']
        if 'name' in request.json:
            user_role.name = request.json['name']

        db.session.commit()
        return user_role_schema.dump(user_role)


class UserRoleDeleteResource(Resource):
    def post(self):
        role_id = request.json['role_id']
        user_role = UserRole.query.get_or_404(role_id)

        affected_users = User.query.filter_by('role_id' == role_id)


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

api.add_resource(UserResource, '/api/v1/users/<user_id>')
api.add_resource(UserListResource, '/api/v1/users/')
api.add_resource(UserNumberListResource, '/api/v1/users/id-list')
api.add_resource(UserCreationResource, '/api/v1/users/create')
api.add_resource(UserPatchResource, '/api/v1/users/update')
api.add_resource(UserDeleteResource, '/api/v1/users/delete')

# ------------------------------------------------
#                      UserRole
# ------------------------------------------------

api.add_resource(UserRoleResource, '/api/v1/user_roles/<role_id>')
api.add_resource(UserRoleListResource, '/api/v1/user_roles/')
api.add_resource(UserRoleCreationResource, '/api/v1/user_roles/create')
api.add_resource(UserRolePatchResource, '/api/v1/user_roles/update')
api.add_resource(UserRoleDeleteResource, '/api/v1/user_roles/delete')