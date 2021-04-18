from typing import Optional
from datetime import datetime

from app.db import shows
from .base import BaseRepository
from app.models.show import Show

class ShowRepository(BaseRepository):
    async def get_list(self,
                 chanel_id: int,
                 start_t: datetime,
                 end_t: datetime
                 ) -> list[Show]:
        query = shows.select().where(shows.c.chanel_id==chanel_id)
        if start_t:
            query = query.where(shows.c.start_t >= start_t)
        if end_t:
            query = query.where(shows.c.end_t <= end_t)

        return await self.database.fetch_all(query=query)
