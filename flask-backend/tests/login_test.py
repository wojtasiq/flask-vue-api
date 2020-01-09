#!flask/bin/python
import os
import unittest

from app import app
from services.database import db
from argon2 import PasswordHasher
import app_init
from models.user import ModelUser, ModelLoginHistory


class LoginTestCase(unittest.TestCase):

    def setUpClass():
        app.config.from_object('config.default')
        app.config.from_object('config.test')
        app.app_context().push()
        app_init.init_app()

    def setUp(self):
        self.client = app.test_client()
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

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        os.remove('../test.db.sqlite')
        pass

    def test_login_path(self):
        parameter = {'username': 'wojtasiq', 'password': 'wojtasiq'}
        response = self.client.post('/login', json=parameter, headers={'content-type': 'application/json'})

        self.assertEqual(response.status_code, 200)

    def test_login_correct(self):
        parameter = {'username': 'wojtasiq', 'password': 'wojtasiq'}
        response_json = self.client.post('/login', json=parameter, headers={'content-type': 'application/json'}).json

        self.assertTrue('token' in response_json)

    def test_login_incorrect(self):
        parameter = {'username': 'wrong', 'password': 'wrong'}
        response_json = self.client.post('/login', json=parameter, headers={'content-type': 'application/json'}).json

        self.assertFalse('token' in response_json)

    def test_login_history(self):
        parameter = {'username': 'wojtasiq', 'password': 'wojtasiq'}
        user_pre_login = ModelUser.query.filter_by(username='wojtasiq').first()

        user_history_count = len(user_pre_login.login_history)

        response_json = self.client.post('/login', json=parameter, headers={'content-type': 'application/json'}).json

        user_after_login = ModelUser.query.filter_by(username='wojtasiq').first()
        user_history_count_after = len(user_after_login.login_history)
        user_history_count = user_history_count + 1

        self.assertEqual(user_history_count, user_history_count_after)


if __name__ == '__main__':
    unittest.main()
