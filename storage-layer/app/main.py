from fastapi import FastAPI

import app.pg as pg
from app.models import Subscription

app = FastAPI()

@app.post("/subscription/")
def create_subscription(sub: Subscription):
    pg.upsert_subscription(sub)
    return sub

@app.get("/initdb")
async def init_db():
    pg.setup_db()
    return 200
