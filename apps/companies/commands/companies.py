from sqlalchemy.orm import Session

from apps.companies.models.companies import Company


def create_compamny(db: Session):
    company = Company(name="JYP")
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
