from app.repositories.chanels import ChanelRepository
from app.db.base import database

def get_chanels() -> ChanelRepository:
    return ChanelRepository(database)