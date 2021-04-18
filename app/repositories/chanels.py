from app.db import chanels
from .base import BaseRepository
from app.models.chanel import Chanel

class ChanelRepository(BaseRepository):
    async def get_all(self) -> list[Chanel]:
        query = chanels.select()
        return await self.database.fetch_all(query=query)

