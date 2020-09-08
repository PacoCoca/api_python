from api_python.services import public
from api_python import middlewares

from werkzeug.exceptions import Unauthorized, BadRequest
from flask import Blueprint, g, request, make_response
import json


bp = Blueprint('public', __name__, url_prefix='/public')


@bp.route('', methods=('GET',), defaults={'public_id': None})
@bp.route('/<int:public_id>', methods=('GET',))
def read(public_id):
    # Anyone can read the publics objects
    publics = json.dumps(public.read(public_id))

    response = make_response(publics, 200)
    response.mimetype = 'application/json'
    return response


@bp.route('', methods=('POST',))
# Only logged users can create new publics
@middlewares.is_logged
def create():
    body = request.json
    if body is None:
        raise BadRequest()

    try_create = public.create(
        field1=body['field1'] if 'field1' in body.keys() else None,
        field2=body['field2'] if 'field2' in body.keys() else None
    )

    if try_create == 'Bad Request':
        raise BadRequest()

    response = make_response(try_create, 200)
    response.mimetype = 'text/plain'
    return response


@bp.route('/<int:public_id>', methods=('PUT',))
# Only logged users can update publics
@middlewares.is_logged
def update(public_id):
    body = request.json
    if body is None:
        raise BadRequest()

    try_update = public.update(
        public_id=public_id,
        field1=body['field1'] if 'field1' in body.keys() else None,
        field2=body['field2'] if 'field2' in body.keys() else None
    )
    if try_update == 'Bad Request':
        raise BadRequest()

    response = make_response(try_update, 200)
    response.mimetype = 'text/plain'
    return response


@bp.route('/<int:public_id>', methods=('DELETE',))
# Only logged admin users can delete publics
@middlewares.is_logged
@middlewares.user_data
def delete(public_id):
    if (g.user['type'] != 'admin'):
        raise Unauthorized()

    try_delete = public.delete(public_id)

    response = make_response(try_delete, 200)
    response.mimetype = 'text/plain'
    return response
