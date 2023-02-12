from sqlalchemy.orm import Session, joinedload

from apps.singers.models.singers import Singer


def get_singers(db: Session):
    singers = db.query(Singer).options(joinedload(Singer.company)).all()
    return singers
