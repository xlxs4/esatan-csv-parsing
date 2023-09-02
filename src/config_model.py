from pydantic import BaseModel


class Config(BaseModel):
    filename: str
