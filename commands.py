from sqlalchemy.orm import Session

from bodies import CityBody, TownBody
from models import City, Town


def create_city(db: Session, city_body: CityBody):
    city = City()
    city.name = city_body.name
    db.add(city)
    db.commit()
    db.refresh(city)
    return city


def create_town(db: Session, town_body: TownBody):
    town = Town()
    town.city_id = town_body.city_id
    town.name = town_body.name
    db.add(town)
    db.commit()
    db.refresh(town)
    return town
