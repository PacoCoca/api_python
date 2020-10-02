import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    Create the connection with the database if doesn't exist
    in the current request and return it

    Returns
    -------
    connection
        The connection with the database
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Close the database connection"""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    """
    Make sure the connection is closed after the request is finished
    and add a command to create the db.

    Parameters
    ----------
    app : Flask
        The Flask app in which makes the changes
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    """Create the database schema"""
    db = get_db()

    with current_app.open_resource('database/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
