from pydantic import BaseModel, IPvAnyAddress
class DBCredentials(BaseModel):
    db_server: str
    username: str
    password: str
    db_name: str
    host: str
    port: int