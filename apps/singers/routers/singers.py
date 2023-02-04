from typing import List

from configs.databases import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.singers.models.singers import Singer

router = APIRouter()
