import os
from dotenv import load_dotenv
from app import app
from argon2 import PasswordHasher
import app_init
load_dotenv()

app.config.from_object('config.default')
app.config.from_object(os.environ.get('CONFIG_FILE'))
app.app_context().push()
app_init.init_app()

from services.database import db
from models.user import ModelUser, ModelLoginHistory

response = input('This will purge database, continue? (Y/N)')

if response != 'y' and response != 'Y':
    print('Fixtures Aborted')
    exit(0)

db.drop_all()
db.create_all()

ph = PasswordHasher()

# Users
user = ModelUser(username='wojtasiq', password=ph.hash('wojtasiq'), name='Wojciech', surname='Wójcik')

login1 = ModelLoginHistory()
login2 = ModelLoginHistory()

user.login_history.append(login1)
user.login_history.append(login2)

db.session.add(user)
db.session.commit()

print('FIXTURES LOADED')
