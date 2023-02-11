from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.companies.models.companies import Company
from apps.configs.databases import get_db

router = APIRouter(prefix="/companies")


@router.post(path="")
def create_singer(db: Session = Depends(get_db)):
    company = Company(name="SM")
    db.add(company)
    db.commit()
    db.refresh(company)
    print(company.id, company.name, company.created_at)
    return {"message": "hihi"}
