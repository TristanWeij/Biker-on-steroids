import sqlite3

import click
from flask import current_app, g


def database():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init():
    db = database()

    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))


@click.command('init-db')
def init_command():
    init()
    click.echo('Initialized database.')


def init_app(app):
    app.teardown_appcontext(close)
    app.cli.add_command(init_command)
