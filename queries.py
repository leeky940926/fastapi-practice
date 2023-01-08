from sqlalchemy.orm import Session

from models import City, Town


def get_town_list(db: Session) -> list:
    return db.query(Town).all()


def get_city_list(db: Session) -> list:
    return db.query(City).all()
