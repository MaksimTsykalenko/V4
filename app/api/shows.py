from typing import Optional
from fastapi import APIRouter, Depends
from datetime import datetime
from app.repositories.shows import ShowRepository
from app.api.dependencies.shows import get_shows

router = APIRouter()

@router.get("/{ch_id}")
async def get_shows(ch_id: int,
        start_t: Optional[datetime]=None,
        end_t: Optional[datetime]=None,
        shows: ShowRepository = Depends(get_shows)):
    return await shows.get_list(chanel_id=ch_id,start_t=start_t, end_t=end_t)
