from api_python.database.db import get_db


def read(public_id=None):
    """
    Read the public resource identified by public_id, or all of them if not specified

    Parameters
    ----------
    public_id : int, optional
        The id of the public resource

    Returns
    -------
    list(dict)
        A list with dictionary/ies with the data of the public resource/s
    """
    db = get_db()
    if public_id is None:
        rows = [dict(row) for row in db.execute(
            'SELECT * FROM `public`'
        ).fetchall()]
    else:
        rows = [dict(row) for row in db.execute(
            'SELECT * FROM `public` WHERE `id`=?', (public_id,)
        ).fetchall()]

    return rows


def create(field1=None, field2=None):
    """
    Create a public resource, at least 1 parameter must be passed

    Parameters
    ----------
    field1 : str, optional
    field2 : str, optional

    Returns
    -------
    str
        string indicating the operation result
    """
    if field1 is None and field2 is None:
        return 'Bad Request'

    db = get_db()
    db.execute(
        'INSERT INTO `public`(`field1`, `field2`) VALUES(?, ?)', (field1, field2)
    )
    db.commit()

    return 'ok'


def update(public_id, field1=None, field2=None):
    """
    Update the public resource identified by public_id, 
    at least 1 more parameter must be passed

    Parameters
    ----------
    public_id : int
    field1 : str, optional
    field2 : str, optional

    Returns
    -------
    str
        string indicating the operation result
    """
    if field1 is None and field2 is None:
        return 'Bad Request'

    db = get_db()
    db.execute(
        'UPDATE `public` SET `field1`=?, `field2`=? WHERE `id`=?',
        (field1, field2, public_id)
    )
    db.commit()

    return 'ok'


def delete(public_id):
    """
    Delete the public resource identified by public_id

    Parameters
    ----------
    public_id : int

    Returns
    -------
    str
        string indicating the operation result
    """
    db = get_db()
    db.execute(
        'DELETE FROM `public` WHERE `id`=?', (public_id,)
    )
    db.commit()

    return 'ok'
