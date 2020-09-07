from api_python.services import auth


from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import Unauthorized
import functools
from flask import Blueprint, g, request, make_response

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('POST',))
def login():
    try_log = auth.login(
        email=request.json['email'],
        password=request.json['password']
    )

    if (try_log == 'Wrong Credentials'):
        raise Unauthorized()

    response = make_response(try_log, 200)
    response.mimetype = 'text/plain'

    return response
