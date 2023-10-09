from fastapi import APIRouter
from . import schemas, database
router = APIRouter()


@router.post("/connect_db/")
async def connect_db(credentials: schemas.DBCredentials) -> schemas.DBCredentials:
    database.create_db_connection(credentials)
    return credentials