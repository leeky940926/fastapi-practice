from sqlalchemy.orm import Session

from apps.singers.models.singers import Singer


def create_singer(db: Session):
    singer = Singer(name="BTS", company_id=1)
    db.add(singer)
    db.commit()
    db.refresh(singer)
    return singer
