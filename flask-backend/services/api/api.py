from flask_restplus import Api
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from jwt.exceptions import ExpiredSignatureError
from werkzeug.exceptions import Unauthorized, BadRequest

api = Api()


@api.errorhandler(NoAuthorizationError)
def no_jwt_token(error):
    raise Unauthorized()


@api.errorhandler(ExpiredSignatureError)
def no_jwt_token(error):
    raise Unauthorized()


@api.errorhandler(InvalidHeaderError)
def bad_authorization_header(error):
    raise BadRequest()
