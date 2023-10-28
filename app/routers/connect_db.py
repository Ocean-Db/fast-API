from fastapi import APIRouter

from . import database, schemas

router = APIRouter()


@router.post('/connect_db/')
async def connect_db(credentials: schemas.DBCredentials) -> schemas.DBCredentials:
    if credentials.db_server == 'mongodb+srv':
        database.create_mongodb_connection(credentials)
    else:
        database.create_db_connection(credentials)
    return credentials
