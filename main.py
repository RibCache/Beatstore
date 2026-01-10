from fastapi import FastAPI
from src.routers.auth import router
from src.db.database import Base, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)

app.include_router(router)