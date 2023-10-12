from pydantic import BaseModel, IPvAnyAddress
from typing import Literal


class DBCredentials(BaseModel):
    db_server: Literal["mysql+pymysql", "mysql+pymysql", "mongodb"]
    username: str
    password: str
    db_name: str
    host: str
    port: int