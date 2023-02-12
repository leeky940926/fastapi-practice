from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.configs.databases import get_db
from apps.singers.commands.singers import create_singer
from apps.singers.quries.singers import get_singers

router = APIRouter(prefix="/singers")


@router.post(path="")
def post(db: Session = Depends(get_db)):
    singer = create_singer(db=db)
    result = {
        "id": singer.id,
        "created_at": singer.created_at,
        "name": singer.name,
        "company_id": singer.company_id,
        "company_name": singer.company.name,
    }
    return result


@router.get(path="")
def get(db: Session = Depends(get_db)):
    singer_list = get_singers(db=db)
    result = {"result": singer_list}
    return result
