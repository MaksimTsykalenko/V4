from fastapi import APIRouter,Depends
from app.repositories.chanels import ChanelRepository
from app.api.dependencies.chanels import get_chanels
router = APIRouter()

@router.get("/")
async def get_chanels(chanels: ChanelRepository= Depends(get_chanels)):
    return await chanels.get_all()
