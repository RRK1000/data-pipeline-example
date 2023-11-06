from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi_route_log.log_request import LoggingRoute

import uvicorn
import pg
from models import Subscription
import simplejson as json


# FastAPI specific code
app = FastAPI()

@app.post("/subscription/")
def create_subscription(sub: Subscription):
    pg.upsert_subscription(sub)
    return sub


@app.get("/initdb")
async def init_db():
    pg.setup_db()
    return 200


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
