from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bodies import CityBody
from commands import create_city
from databases import get_db
from queries import get_city_list
from schemas import CitySchema

router = APIRouter()


@router.post("/cities", response_model=CitySchema)
async def create_cities(city_body: CityBody, db: Session = Depends(get_db)):
    return create_city(db=db, city_body=city_body)


@router.get("/cities", response_model=List[CitySchema])
async def get_cities(db: Session = Depends(get_db)):
    return get_city_list(db=db)
