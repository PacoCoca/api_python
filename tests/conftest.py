import os
import tempfile

import pytest
from api_python import create_app
from api_python.database.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    """
    Class to log in without using too much boilerplate.
    This class is useful since many methods require to be logged
    """

    def __init__(self, client):
        self._client = client

    def login(self, email='foo@foo.foo', password='bar'):
        response = self._client.post(
            '/auth/login',
            json={'email': email, 'password': password}
        )
        return response.get_data().decode('utf-8') if response.status_code == 200 else ''


@pytest.fixture
def auth(client):
    return AuthActions(client)
