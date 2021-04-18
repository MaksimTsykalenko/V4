from fastapi import FastAPI
import uvicorn

from app.db.base import database
from app.api import chanels,shows

app=FastAPI()
app.include_router(chanels.router, prefix="/chanels", tags=["chanels"])
app.include_router(shows.router, prefix="/shows", tags=["shows"])

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)


