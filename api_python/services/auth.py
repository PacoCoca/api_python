from api_python.database.db import get_db
from api_python.config.env import env

import time
import jwt


def login(email, password):
    db = get_db()

    user = db.execute(
        'SELECT `password` FROM `user` WHERE `email`=?', (email,)
    ).fetchone()

    if user is None or not check_password_hash(user['password'], password):
        return 'Wrong Credentials'

    # issued time of the token
    iat = time.time()
    db.execute(
        'UPDATE user SET iat=FROM_UNIXTIME(?) WHERE email=?', (iat, email)
    )
    db.commit()

    payload = {
        'iat': iat,
        'email': email
    }
    token = jwt.encode(payload, env['auth']['key'], algorithm='HS256')

    return token
