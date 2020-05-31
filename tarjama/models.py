from sqlalchemy import create_engine, Column, Integer, String, DateTime
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
    date = Column(DateTime, nullable=False)

    @classmethod
    def insert(cls, record):
        # insert word with its translation
        with session_scope() as session:
            print('Inserting word...')
            session.add(record)

            # update database to get id of inserted word
            session.flush()
            pk = record.id

        return pk

    @classmethod
    def retrieve_all(cls):
        # retrieve all words
        with session_scope() as session:
            print('Retrieving all words...')
            records = session.query(cls).all()
            session.expunge_all()

        return records

    @classmethod
    def update_by_id(cls, pk, word, translation):
        # update word by id
        with session_scope() as session:
            print('Updating word...')
            record = session.query(cls).get(pk)
            record.word = word
            record.translation = translation

    @classmethod
    def retrieve_by_id(cls, pk):
        # retrieve word by id
        with session_scope() as session:
            print('Retrieving word...')
            record = session.query(cls).get(pk)
            session.expunge_all()

        return record

    @classmethod
    def delete_by_id(cls, pk):
        # delete word by id
        with session_scope() as session:
            print('Deleting word...')
            record = session.query(cls).get(pk)
            session.delete(record)


# create table if non-existing
Base.metadata.create_all(engine)
