from sqlalchemy import URL, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from . import schemas

Base = declarative_base()


def create_db_connection(credentials: schemas.DBCredentials):
    global engine, SessionLocal
    DATABASE_URL = URL.create(
        drivername=credentials.db_server,
        username=credentials.username,
        password=credentials.password,
        host=credentials.host,
        port=credentials.port,
        database=credentials.db_name,
    )

    engine = create_engine(DATABASE_URL)

    try:
        engine.connect()
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine)
    except SQLAlchemyError as se:
        pass
