from pydantic import BaseModel

class Subscription(BaseModel):
    username: str
    payment_method: str
    plan: str
    status: str
    term: str

