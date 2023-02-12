from sqlalchemy.orm import Session, joinedload

from apps.albums.models.albums import Album


def get_albums(db: Session):
    albums = db.query(Album).options(joinedload("singer"), joinedload("singer.company"))
    print(albums.statement)
    albums = albums.all()
    return albums
