from api_python.database.db import get_db


def read(private_id=None):
    """
    Read the private resource identified by private_id, or all of them if not specified

    Parameters
    ----------
    private_id : int, optional
        The id of the private resource

    Returns
    -------
    list(dict)
        A list with dictionary/ies with the data of the private resource/s
    """
    db = get_db()
    if private_id is None:
        rows = [dict(row) for row in db.execute(
            'SELECT * FROM `private`'
        ).fetchall()]
    else:
        rows = [dict(row) for row in db.execute(
            'SELECT * FROM `private` WHERE `id`=?', (private_id,)
        ).fetchall()]

    return rows


def create(field1=None, field2=None):
    """
    Create a private resource, at least 1 parameter must be passed

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
        'INSERT INTO `private`(`field1`, `field2`) VALUES(?, ?)', (field1, field2)
    )
    db.commit()

    return 'ok'


def update(private_id, field1=None, field2=None):
    """
    Update the private resource identified by private_id, 
    at least 1 more parameter must be passed

    Parameters
    ----------
    private_id : int
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
        'UPDATE `private` SET `field1`=?, `field2`=? WHERE `id`=?',
        (field1, field2, private_id)
    )
    db.commit()

    return 'ok'


def delete(private_id):
    """
    Delete the private resource identified by private_id

    Parameters
    ----------
    private_id : int

    Returns
    -------
    str
        string indicating the operation result
    """
    db = get_db()
    db.execute(
        'DELETE FROM `private` WHERE `id`=?', (private_id,)
    )
    db.commit()

    return 'ok'
