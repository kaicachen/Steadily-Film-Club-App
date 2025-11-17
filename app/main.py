from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router

app = FastAPI(title="Film Club API")
app.include_router(router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
