from api_python.database.db import get_db
from api_python.config.env import env

import jwt
from werkzeug.security import generate_password_hash


def user_data(token):
    """
    Get the data of the user identified by a token

    Parameters
    ----------
    token : JWT
        The token with the user credentials

    Returns
    -------
    dict
        A dict with the user info
    """
    decoded = jwt.decode(token, env['auth']['key'], algorithms=['HS256'])
    email, iat = decoded['email'], decoded['iat']

    db = get_db()
    return dict(
        db.execute('SELECT * FROM `user` WHERE `email`=?', (email,)).fetchone()
    )


def create(email, password, user_type=None):
    """
    Create a user

    Parameters
    ----------
    email : str
    password : str
    user_type : str, optional
        Can be either 'user' or 'admin'

    Returns
    -------
    str
        string indicating the operation result
    """
    if email is None or password is None:
        return 'Bad Request'

    db = get_db()
    db.execute(
        'INSERT INTO `user`(`email`, `password`, `type`) VALUES(?, ?, ?)',
        (email, generate_password_hash(password), user_type)
    )
    db.commit()

    return 'ok'
