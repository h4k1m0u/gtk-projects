from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager


# connect to database file & create classes needed
engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


# separate management of session lifecycle
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html
@contextmanager
def session_scope():
    # define function for with-statement
    session = Session()

    try:
        # trigger with-statement block after generator yields
        yield session

        # run after with-statement block
        session.commit()
    except Exception as e:
        # catch exceptions in try or with blocks
        session.rollback()

        # raise exception to halt execution (after finally)
        raise e
    finally:
        session.close()


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)

    def insert(self, session):
        session.add(self)


# create table if non-existing
Base.metadata.create_all(engine)
