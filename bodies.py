from pydantic import BaseModel


class TownBody(BaseModel):
    city_id: int
    name: str


class CityBody(BaseModel):
    name: str
