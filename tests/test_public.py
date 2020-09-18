import pytest
import json


@pytest.mark.parametrize('public_id', (
    (1),  # This value exists
    (8),  # This value doesn't
    (None),
))
def test_read(client, public_id):
    path = '/public' if public_id is None else f'/public/{public_id}'
    response = client.get(path)

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


@pytest.mark.parametrize('email, password, field1, field2', (
    ('foo@foo.foo', 'bar', 'test 1', 'test 1'),
    ('foo2@foo.foo', 'bar', 'test 2', ''),
    ('error@foo.foo', 'bar', 'test 3 ', 'test 3'),
))
def test_create(auth, client, email, password, field1, field2):
    token = auth.login(email, password)

    body = {
        "field1": field1,
        "field2": field2,
    }
    response = client.post(
        '/public',
        data=json.dumps(body),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'Application/json'
        },
    )

    if len(token) == 0:
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'


@pytest.mark.parametrize('email, password, public_id, field1, field2', (
    ('foo@foo.foo', 'bar', 1, 'test 1', 'test 1'),
    ('foo2@foo.foo', 'bar', 8, 'test 2', ''),
    ('error@foo.foo', 'bar', 1, 'test 3 ', 'test 3'),
))
def test_update(auth, client, email, password, public_id, field1, field2):
    token = auth.login(email, password)

    body = {
        "field1": field1,
        "field2": field2,
    }
    response = client.put(
        f'/public/{public_id}',
        data=json.dumps(body),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'Application/json'
        },
    )

    if len(token) == 0:
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'


@pytest.mark.parametrize('email, password, public_id', (
    ('foo@foo.foo', 'bar', 1),
    ('foo2@foo.foo', 'bar', 8),
    ('error@foo.foo', 'bar', 1),
))
def test_delete(auth, client, email, password, public_id):
    token = auth.login(email, password)

    response = client.delete(
        f'/public/{public_id}',
        headers={
            'Authorization': f'Bearer {token}'
        },
    )

    # Only admins can delete
    if len(token) == 0 or email != "foo@foo.foo":
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'
