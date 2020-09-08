from api_python.services import auth

import functools
from werkzeug.exceptions import Unauthorized
from jwt import InvalidSignatureError
from flask import Blueprint, g, request, make_response


def is_logged(f):
    """Check if the user is providing a valid token

    Parameters
    ----------
    f : function
        The function that need the user to be logged

    Returns
    -------
    function
        The same function but asserting the token is valid
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
