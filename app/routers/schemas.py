from typing import Literal

from pydantic import BaseModel


class DBCredentials(BaseModel):
    db_server: Literal['mysql+pymysql', 'postgresql+psycopg2', 'mongodb+srv']
    username: str
    password: str
    db_name: str
    host: str
    port: int
