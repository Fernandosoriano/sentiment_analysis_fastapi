from pydantic import BaseModel
from datetime import datetime
class Sentiment(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: datetime
