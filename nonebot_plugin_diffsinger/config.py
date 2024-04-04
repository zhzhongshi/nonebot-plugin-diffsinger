from pydantic import BaseModel


class Config(BaseModel):
    ds_url: str = "http://127.0.0.1:9266/"
    ds_speedup: int = 200
