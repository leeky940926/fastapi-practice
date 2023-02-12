from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.companies.commands.companies import create_compamny
from apps.configs.databases import get_db

router = APIRouter(prefix="/companies")


@router.post(path="")
def post(db: Session = Depends(get_db)):
    company = create_compamny(db=db)
    result = {"id": company.id, "created_at": company.created_at, "name": company.name}
    return result
