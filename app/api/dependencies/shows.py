from app.repositories.shows import ShowRepository
from app.db.base import database

def get_shows() -> ShowRepository:
    return ShowRepository(database)