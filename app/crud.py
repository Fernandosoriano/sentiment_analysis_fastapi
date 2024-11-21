from sqlalchemy.orm import Session
from app import models

def create_sentiment(db: Session, text: str, sentiment: str):
    sentiment_entry = models.Sentiment(text=text, sentiment=sentiment)
    db.add(sentiment_entry)
    db.commit()
    db.refresh(sentiment_entry)
    return sentiment_entry

def get_sentiments(db: Session):
    return db.query(models.Sentiment).all()
