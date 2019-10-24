import click

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask.cli import with_appcontext

from config import dbconf

db_session = {}
engine = {}
Base = {}


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
    global db_session, Base, engine

    engine = create_engine(dbconf.get('dsn'), convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()

    app.teardown_appcontext(db_session.remove)
    app.cli.add_command(reset_db_command)
