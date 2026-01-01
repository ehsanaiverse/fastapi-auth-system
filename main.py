from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import Base, engine
from routers import router as user_account


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

# home routes --> endpoint
@app.get('/')
def home():
    return {'message': 'Welcome to the FastAPI Authentication System'}


# users routes
app.include_router(user_account)
