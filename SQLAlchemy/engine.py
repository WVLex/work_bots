from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, MetaData
from contextlib import contextmanager


url = 'hidden'
engine = create_engine(url)
meta = MetaData(engine)
Base = declarative_base(engine)


@contextmanager
def session_scope():
    session = Session(engine, future=True)
    try:
        yield session
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()
