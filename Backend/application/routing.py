from functools import partial
import sqlalchemy.orm as orm
from flask_sqlalchemy import SQLAlchemy, get_state
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from logger import set_logging

log = set_logging("db_routing.log")


class AutoRouteSession(orm.Session):

    def __init__(self, db, autocommit=False, autoflush=False, **options):
        self.app = db.get_app()
        self._model_changes = {}
        orm.Session.__init__(self, autocommit=autocommit, autoflush=autoflush,
                             bind=db.engine,
                             binds=db.get_binds(self.app), **options)

    def get_bind(self, mapper=None, clause=None):

        try:
            state = get_state(self.app)
        except (AssertionError, AttributeError, TypeError) as err:
            log.info(
                "Unable to get Flask-SQLAlchemy configuration. Outputting default bind. Error:" + err)
            return orm.Session.get_bind(self, mapper, clause)

        # If there are no binds configured, connect using the default SQLALCHEMY_DATABASE_URI
        if state is None or not self.app.config['SQLALCHEMY_BINDS']:
            if not self.app.debug:
                log.debug(
                    "Connecting -> DEFAULT. Unable to get Flask-SQLAlchemy bind configuration. Outputting default bind.")
            return orm.Session.get_bind(self, mapper, clause)

        # Writes go to the master
        elif self._flushing:  # we who are about to write, salute you
            log.debug("Connecting -> MASTER")
            return state.db.get_engine(self.app, bind='master')

        # 5-5 distribution for Read operation
        else:
            if random.randint(0, 1) < 1:
                bind_name = 'slave'
            else:
                bind_name = 'master'

            log.debug("Connecting -> {}".format(bind_name.upper()))
            return state.db.get_engine(self.app, bind=bind_name)


class AutoRouteSQLAlchemy(SQLAlchemy):

    def create_scoped_session(self, options=None):
        """Helper factory method that creates a scoped session."""
        if options is None:
            options = {}
        scopefunc = options.pop('scopefunc', None)
        return orm.scoped_session(
            partial(AutoRouteSession, self, **options), scopefunc=scopefunc
        )
