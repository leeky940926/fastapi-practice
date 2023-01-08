from datetime import datetime

from pydantic import BaseModel


class CitySchema(BaseModel):
    id: int
    created_at: datetime
    name: str

    class Config:
        orm_mode = True


class TownSchema(BaseModel):
    id: int
    created_at: datetime
    name: str
    city_id: int
    city_name: str

    class Config:
        orm_mode = True
