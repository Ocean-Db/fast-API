from fastapi import APIRouter
from pydantic import BaseModel, IPvAnyAddress

router = APIRouter()


class DBCredentials(BaseModel):
    username: str
    password: str
    db_name: str
    host: IPvAnyAddress
    port: int


@router.post('/connect_db/')
async def connect_db(credentials: DBCredentials) -> DBCredentials:
    return credentials
