from pymongo import MongoClient
from sqlalchemy import URL, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from . import schemas


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
        return engine, SessionLocal
    except SQLAlchemyError as se:
        pass


def create_mongodb_connection(credentials: schemas.DBCredentials):
    MONGO_URI = f'{credentials.db_server}://{credentials.username}:{credentials.password}@{credentials.host}/{credentials.db_name}'
    try:
        client = MongoClient(MONGO_URI)
        db = client.get_database(credentials.db_name)
        return client
    except Exception as e:
        pass
