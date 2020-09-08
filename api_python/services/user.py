from api_python.database.db import get_db
from api_python.config.env import env

import jwt


def user_data(token):
    decoded = jwt.decode(token, env['auth']['key'])
    email, iat = decoded['email'], decoded['iat']

    db = get_db()
    return dict(
        db.execute('SELECT * FROM `user` WHERE `email`=?', (email,)).fetchone()
    )
