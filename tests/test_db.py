from api_python.database.db import get_db

import sqlite3
import pytest


def test_get_db(app):
    """
    """
    # Assert the connection is the same within the same request context
    with app.app_context():
        conn = get_db()
        assert conn is get_db()

    # Assert the connection is closed
    with pytest.raises(sqlite3.ProgrammingError) as e:
        conn.execute('SELECT 1')
    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    """
    """
    class Recorder():
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('api_python.database.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
