import pytest
import json

# Only admins can manipulate private objects


@pytest.mark.parametrize('email, password, private_id', (
    ('foo@foo.foo', 'bar', None),
    ('foo@foo.foo', 'bar', 1),
    ('foo2@foo.foo', 'bar', 8),
    ('foo3@foo.foo', 'bar', None),
))
def test_read(auth, client, email, password, private_id):
    token = auth.login(email, password)

    response = client.get(
        '/private' if private_id is None else f'/private/{private_id}',
        headers={
            'Authorization': f'Bearer {token}'
        },
    )

    if len(token) == 0 or email != "foo@foo.foo":
        assert response.status_code == 401
    else:
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
        '/private',
        data=json.dumps(body),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'Application/json'
        },
    )

    if len(token) == 0 or email != "foo@foo.foo":
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'


@pytest.mark.parametrize('email, password, private_id, field1, field2', (
    ('foo@foo.foo', 'bar', 1, 'test 1', 'test 1'),
    ('foo2@foo.foo', 'bar', 8, 'test 2', ''),
    ('error@foo.foo', 'bar', 1, 'test 3 ', 'test 3'),
))
def test_update(auth, client, email, password, private_id, field1, field2):
    token = auth.login(email, password)

    body = {
        "field1": field1,
        "field2": field2,
    }
    response = client.put(
        f'/private/{private_id}',
        data=json.dumps(body),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'Application/json'
        },
    )

    if len(token) == 0 or email != "foo@foo.foo":
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'


@pytest.mark.parametrize('email, password, private_id', (
    ('foo@foo.foo', 'bar', 1),
    ('foo2@foo.foo', 'bar', 8),
    ('error@foo.foo', 'bar', 1),
))
def test_delete(auth, client, email, password, private_id):
    token = auth.login(email, password)

    response = client.delete(
        f'/private/{private_id}',
        headers={
            'Authorization': f'Bearer {token}'
        },
    )

    if len(token) == 0 or email != "foo@foo.foo":
        assert response.status_code == 401
    else:
        assert response.status_code == 200
        assert response.get_data() == b'ok'
