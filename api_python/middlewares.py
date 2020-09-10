from api_python.services import auth, user

import functools
from werkzeug.exceptions import Unauthorized
from jwt import InvalidSignatureError
from flask import g, request


def is_logged(f):
    """
    Check if the user is providing a valid token

    Parameters
    ----------
    f : function
        The function that need the user to be logged

    Returns
    -------
    function
        The same function but asserting the token is valid

    Raises
    ------
    Unauthorized
        The token is not valid or it is not in the request headers
    """
    @functools.wraps(f)
    def wrapped(**kwargs):
        try:
            # The authorization header has the form: "Authorization": "Bearer " + JWT
            token = request.headers['Authorization'].split(' ')[1]
            if not auth.check_token(token):
                raise Unauthorized()
            return f(**kwargs)
        except (InvalidSignatureError, KeyError):
            # If the JWT is invalid or the Authorization header is not provided,
            # just send Unuathorized response
            raise Unauthorized()

    return wrapped


def user_data(f):
    """
    Save the user data in g

    Parameters
    ----------
    f : function
        The function that need the user data

    Returns
    -------
    function
        The same function but first it attaches the user data to g (Global object to the request)
    """
    @functools.wraps(f)
    def wrapped(**kwargs):
        token = request.headers['Authorization'].split(' ')[1]
        g.user = user.user_data(token)

        return f(**kwargs)

    return wrapped
