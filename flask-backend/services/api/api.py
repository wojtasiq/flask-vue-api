from flask_restplus import Api
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError
from werkzeug.exceptions import Unauthorized

api = Api()


@api.errorhandler(NoAuthorizationError)
def no_jwt_token(error):
    raise Unauthorized()


@api.errorhandler(ExpiredSignatureError)
def no_jwt_token(error):
    raise Unauthorized()
