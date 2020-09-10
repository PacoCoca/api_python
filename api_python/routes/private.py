from api_python.services import private
from api_python import middlewares

from werkzeug.exceptions import Unauthorized, BadRequest
from flask import Blueprint, g, request, make_response
import json


# Only admins can manipulate private objects
bp = Blueprint('private', __name__, url_prefix='/private')


@bp.route('', methods=('GET',), defaults={'private_id': None})
@bp.route('/<int:private_id>', methods=('GET',))
@middlewares.is_logged
@middlewares.user_data
def read(private_id):
    if (g.user['type'] != 'admin'):
        raise Unauthorized()

    privates = json.dumps(private.read(private_id))

    response = make_response(privates, 200)
    response.mimetype = 'application/json'
    return response


@bp.route('', methods=('POST',))
@middlewares.is_logged
@middlewares.user_data
def create():
    if (g.user['type'] != 'admin'):
        raise Unauthorized()

    body = request.json
    if body is None:
        raise BadRequest()

    try_create = private.create(
        field1=body['field1'] if 'field1' in body.keys() else None,
        field2=body['field2'] if 'field2' in body.keys() else None
    )

    if try_create == 'Bad Request':
        raise BadRequest()

    response = make_response(try_create, 200)
    response.mimetype = 'text/plain'
    return response


@bp.route('/<int:private_id>', methods=('PUT',))
@middlewares.is_logged
@middlewares.user_data
def update(private_id):
    if (g.user['type'] != 'admin'):
        raise Unauthorized()

    body = request.json
    if body is None:
        raise BadRequest()

    try_update = private.update(
        private_id=private_id,
        field1=body['field1'] if 'field1' in body.keys() else None,
        field2=body['field2'] if 'field2' in body.keys() else None
    )
    if try_update == 'Bad Request':
        raise BadRequest()

    response = make_response(try_update, 200)
    response.mimetype = 'text/plain'
    return response


@bp.route('/<int:private_id>', methods=('DELETE',))
@middlewares.is_logged
@middlewares.user_data
def delete(private_id):
    if (g.user['type'] != 'admin'):
        raise Unauthorized()

    try_delete = private.delete(private_id)

    response = make_response(try_delete, 200)
    response.mimetype = 'text/plain'
    return response
