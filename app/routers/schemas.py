from pydantic import BaseModel


class DBCredentials(BaseModel):
    db_server: str
    username: str
    password: str
    db_name: str
    host: str
    port: int
