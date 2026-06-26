import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DB_URL")

engine = create_engine(str(db_url))

local_session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def check_connection():
    from sgr.storage.models.game import Game as Game

    print(Game)
