from services.database import db
from services.jwt import jwt
from services.api.api import api
from app import app


def init_app():
    init_db()
    init_api()
    init_jwt()
    init_routes()


def init_db():
    db.init_app(app)
    from models.user import ModelUser, ModelLoginHistory


def init_api():
    api.init_app(app)


def init_jwt():
    jwt.init_app(app)


def init_routes():
    import services.api.routes.routes
