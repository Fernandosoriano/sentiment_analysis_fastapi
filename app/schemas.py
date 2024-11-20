from pydantic import BaseModel
from datetime import datetime

class SentimentCreate(BaseModel):
    text: str

class Sentiment(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: datetime

    class Config:
        orm_mode = True
