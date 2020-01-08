from flask_restplus import Resource, marshal
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask import jsonify, request
from services.api.api import api
from helpers.user_marshals import login_history_fields, user_data_fields
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.exceptions import BadRequest, Unauthorized
from models.user import ModelUser, ModelLoginHistory
from services.database import db


@api.route('/login')
class Login(Resource):
    @api.param('username')
    @api.param('password')
    def post(self):
        json_data = request.get_json()

        if 'password' not in json_data or 'username' not in json_data:
            raise BadRequest('No username or password provided')

        username = json_data['username']
        password = json_data['password']

        user = ModelUser.query.filter_by(username=username).first()

        if user is None:
            raise Unauthorized()

        try:
            ph = PasswordHasher()
            ph.verify(user.password, password)
        except VerifyMismatchError:
            raise Unauthorized()

        user.login_history.append(ModelLoginHistory())
        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=username)
        return jsonify({'token': token})


@api.route('/auth/user/login_history')
class LoginHistory(Resource):
    @jwt_required
    def get(self):
        identity = get_jwt_identity()

        user = ModelUser.query.filter_by(username=identity).first()

        login_list = user.login_history
        return jsonify({'loginDates': [marshal(login, login_history_fields) for login in login_list]})


@api.route('/auth/user/me')
class LoginHistory(Resource):
    @jwt_required
    def get(self):
        identity = get_jwt_identity()

        user = ModelUser.query.filter_by(username=identity).first()

        return jsonify({'user': marshal(user, user_data_fields)})
