import click

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask.cli import with_appcontext
from flask import current_app

engine = create_engine(current_app.config.get('db').get('dsn'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def reset_db():
    import models
    Base.metadata.create_all(bind=engine)


@click.command('reset-db')
@with_appcontext
def reset_db_command():
    """Clear the existing data and create new tables."""
    reset_db()
    click.echo('Reset the database.')


def init_db(app):
    app.teardown_appcontext(db_session.remove)
    app.cli.add_command(reset_db_command)
