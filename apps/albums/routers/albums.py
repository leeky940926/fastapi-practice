from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.albums.queries.albums import get_albums
from apps.configs.databases import get_db

router = APIRouter(prefix="/albums")


@router.get("")
def get_album_list(db: Session = Depends(get_db)):
    albums = get_albums(db=db)
    return {"result": albums}
