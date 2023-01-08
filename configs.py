import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR = os.path.dirname(os.path.abspath("main"))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
