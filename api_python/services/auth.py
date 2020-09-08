from api_python.database.db import get_db
from api_python.config.env import env

from datetime import datetime
import jwt
from werkzeug.security import check_password_hash, generate_password_hash


def login(email, password):
    """Gives the user a JWT to access the data

    Parameters
    ----------
    email - str
        The email of the user
    password - str
        The password of the user

    Returns
    -------
    str
        An error code if an error occurs, or the JWT otherwise
    """
    db = get_db()

    user = db.execute(
        'SELECT `password` FROM `user` WHERE `email`=?', (email,)
    ).fetchone()

    if user is None or not check_password_hash(user['password'], password):
        return 'Wrong Credentials'

    # issued time of the token
    iat = datetime.utcnow().replace(microsecond=0)
    db.execute(
        'UPDATE user SET iat=? WHERE email=?', (iat, email)
    )
    db.commit()

    payload = {
        'iat': iat,
        'email': email
    }
    token = jwt.encode(payload, env['auth']['key'], algorithm='HS256')

    return token


def check_token(token):
    """Checks if a given token is valid

    Parameters
    ----------
    token - str
        The token to verify

    Returns
    -------
    bool
        True if it's valid, False if it isn't
    """
    decoded = jwt.decode(token, env['auth']['key'])
    email, iat = decoded['email'], datetime.utcfromtimestamp(decoded['iat'])
    db = get_db()

    user = db.execute(
        'SELECT `id` FROM `user` WHERE `email`=? AND `iat`=?', (email, iat)
    ).fetchone()

    return user is not None
