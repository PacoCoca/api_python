from api_python.database.db import get_db
from api_python.config.env import env

import jwt


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
    decoded = jwt.decode(token, env['auth']['key'])
    email, iat = decoded['email'], decoded['iat']

    db = get_db()
    return dict(
        db.execute('SELECT * FROM `user` WHERE `email`=?', (email,)).fetchone()
    )
